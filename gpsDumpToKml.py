#!/usr/bin/python3
import sys
import getopt
import gpsLogParser as parser

opts, extraparams = getopt.getopt(sys.argv[1:], "")
gpsData = []


#TODO: "main" function and "help" to print somekind of usage info
for o in extraparams: # this is actually smart as we can give many files to this script
  print("Parsing the file " + o)
  gpsData = parser.parseGpsData(o)
  if gpsData is None:
    print("File \"" + o + "\" failed to be parsed. Skipping.")
    continue
  ##data = readDataFromFile(o)
  ##gpsDataAsString = parseDataToListOfTuples(data)
  # We have now the original data as tuples where data is in string, lets change the data to values where possible
  # tuples are immutable so lets create a new set of tuples
  ##gpsData = handleParsedDataToUsableData(gpsDataAsString)
  # TODO: do something with the data that was read in, like change it into the kml format
  #       and write to file by appending ".kml" to the original filepath.
