#!/usr/bin/python3
import sys
import getopt
from gpsLogParser import GpsLogParser as parser
from kmlBuilder import KMLBuilder


def usage():
  print("Usage: gpsDumpToKml.py [options] [files]")
  print("\nGpsDumpToKml - Parses files made by gpsDump.py and exports the gps data to\nGoogle kml format\n")
  print("Options:")
  print("  --help          Shows this help and exit")
  print("  -v              Verbose")

colors = []
def genColors(minSpeed, maxSpeed, steps):
  # aabbggrr
  step = (maxSpeed - minSpeed) / steps;
  colorStep = int(255/steps)
  for x in range(0,steps):
    alpha = hex(255).split('x')[1]
    blue = "0"
    green = "0"
    red = "f"
    if 255-colorStep*x < 16:
      #blue += hex(colorStep*x).split('x')[1]
      #green += hex(colorStep*x).split('x')[1]
      red += hex(255-colorStep*x).split('x')[1]
    else:
      #blue = hex(colorStep*x).split('x')[1]
      #green = hex(colorStep*x).split('x')[1]
      red = hex(255-colorStep*x).split('x')[1]
    blue = "00"
    green = "00"
    red = "ee"
    # according to google earth, hex ffee0000 is blue
    colors.append((minSpeed + step*x, alpha+red+green+blue))

def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "h:v", ["help", "output="])
  except getopt.GetoptError as err:
    # print help information and exit:
    print(err) # will print something like "option -a not recognized"
    usage()
    sys.exit(2)
  verbose = False
  for o, a in opts:
    if o == "-v":
      verbose = True
    elif o in ("-h", "--help"):
      usage()
      sys.exit()
    else:
      assert False, "unhandled option"
  #print(args)

  for o in args: # this is actually smart as we can give many files to this script or none
    if verbose: print("Parsing the file " + o)
    gpsData = parser.parseGpsData(o)
    if gpsData is None:
      print("File \"" + o + "\" failed to be parsed. Skipping.")
      continue
    #We got data so lets build kml file
    kmlfile = KMLBuilder()
    kmlfile.newKmlFile()

    #Analyze speed for colouring
    maxSpeed = -1
    minSpeed = 100000
    for point in gpsData:
      if (point[0] == 3):
        if point[11] != "nan":
          minSpeed = min(point[11], minSpeed)
          maxSpeed = max(point[11], maxSpeed)

    genColors(int(minSpeed), int(maxSpeed), 20)
    for color in colors:
      kmlfile.addLineStyle("ID" + str(color[0]), color[1], 4)

    cid = 0
    toCoord = None
    fromCoord = None
    for point in gpsData:
      if point[0] == 3:
        if fromCoord is None:
          fromCoord = (point[5],point[4],point[7]+30)
          toCoord = fromCoord
        else:
          toCoord = (point[5],point[4],point[7]+30)
        chosen = -1
        if point[11] != "nan":
          for color in colors:
            if max(int(point[11]), int(color[0])) == int(point[11]):
              chosen +=1
            else:
              break
        else:
          chosen = 0

        kmlfile.addPlacemark(cid, "speed = " + str(point[11]) + "km/h", "ID" + str(colors[chosen][0]), fromCoord, toCoord)
        fromCoord = toCoord
    kmlfile.finalize(o)



    #print(str(colors))
        #print(str(point[5]) + "," + str(point[4]) + "," + str(point[7]))
      #(latitude, longitude, ellipsoidal height)
  ##data = readDataFromFile(o)
  ##gpsDataAsString = parseDataToListOfTuples(data)
  # We have now the original data as tuples where data is in string, lets change the data to values where possible
  # tuples are immutable so lets create a new set of tuples
  ##gpsData = handleParsedDataToUsableData(gpsDataAsString)
  # TODO: do something with the data that was read in, like change it into the kml format
  #       and write to file by appending ".kml" to the original filepath.

if __name__ == "__main__":
  main()
