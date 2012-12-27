#!/usr/bin/python3
import sys
import getopt
from gpsLogParser import GpsLogParser as parser
import kmlBuilder


def usage():
  print("Usage: gpsDumpToKml.py [options] [files]")
  print("\nGpsDumpToKml - Parses files made by gpsDump.py and exports the gps data to\nGoogle kml format\n")
  print("Options:")
  print("  --help          Shows this help and exit")
  print("  -v              Verbose")


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
    for point in gpsData:
      if (point[0] == 3):
        print(str(point[5]) + "," + str(point[4]) + "," + str(point[7]))
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
