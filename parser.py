#!/usr/bin/python3
import sys
import re
import getopt
import ast
opts, extraparams = getopt.getopt(sys.argv[1:], "")
# Regex to match only the original dataformat, yes it's silly and
# no I don't want to do it any other way because reasons
# This ensures that we match data and get tuple with exactly 15 slots.
# This is trivial to change in to the original format
originalFormat = re.compile(r'^\(([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+), ([\w.-]+)\)$')

gpsData = []

def num (s):
  """
    Specialised function to convert int to int and float to float,
    otherwise if such deduction is impossible to do, we return the original string.
    Which in this case usually is that the input is "nan" and not "5" or "0.002"
  """
  try:
    return float(s) if '.' in s else int(s)
    #return ast.literal_eval(s) # as good as above but slow as hell,
                                # still throws ValueError because we have "nan" in data
  except ValueError:
    return s
# Lets read the data from file back to it's original form for easier use

def readDataFromFile(filepath):
  """
    Read the file given to function and returns the content as list of lines.
  """
  try:
    f = open(filepath, 'r')
    data = f.readlines()
    f.close()
    return data
  except IOError:
    print("Reading the file '" + filepath + "' failed")
    return "failed"

def parseDataToListOfTuples(rawData):
  """
    Takes in list of lines and converts them into list of tuples where the data
    is seperated like it is in the original format, which is Tuple of values.
    Instead this function returns the data in format Tuple of strings.
    handleParsedDataToUsableData is used after this format to make the data actually usable.
  """
  gpsDataAsString = []
  for line in rawData:
    #print(line)
    m = originalFormat.match(line)
    if m is not None:
      gpsDataAsString.append(m.groups())
    else:
      gpsDataAsString = []
  return gpsDataAsString

def handleParsedDataToUsableData(parsedData):
  """
  Input is list of tuples where data is still in strings
  Tries to convert everything back to it's corresponding format
  Int to int and float to float, We do have exception that some values are "nan", they are left as so

  dataformat is as follows:
     mode: The mode of the fix
     fields: A bitfield representing which items of this tuple contain valid data
     time: The timestamp of the update (location.GPS_DEVICE_TIME_SET)
     ept: Time accuracy
     latitude: Fix latitude (location.GPS_DEVICE_LATLONG_SET)
     longitude: Fix longitude (location.GPS_DEVICE_LATLONG_SET)
     eph: Horizontal position accuracy
     altitude: Fix altitude in meters (location.GPS_DEVICE_ALTITUDE_SET)
     double epv: Vertical position accuracy
     track: Direction of motion in degrees (location.GPS_DEVICE_TRACK_SET)
     epd: Track accuracy
     speed: Current speed in km/h (location.GPS_DEVICE_SPEED_SET)
     eps: Speed accuracy
     climb: Current rate of climb in m/s (location.GPS_DEVICE_CLIMB_SET)
     epc: Climb accuracy
  """
  usableData = []
  for point in gpsDataAsString:
    usableData.append((num(point[0]),num(point[1]),num(point[2]),num(point[3]),num(point[4]),num(point[5]),num(point[6]),num(point[7]),num(point[8]),num(point[9]),num(point[10]),num(point[11]),num(point[12]),num(point[13]),num(point[14])))
  return usableData;

for o in extraparams: # this is actually smart as we can give many files to this script
  print("Opening " + o)
  data = readDataFromFile(o)
  gpsDataAsString = parseDataToListOfTuples(data)
  # We have now the original data as tuples where data is in string, lets change that
  # tuples are immutable so lets create a new set of tuples
  gpsData = handleParsedDataToUsableData(gpsDataAsString)
  # TODO: do something with the data that was read in, like change it into the kml format
  #       and write to file by appending ".kml" to the original filepath.
