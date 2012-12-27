#!/usr/bin/python3
from kmlHelper import *
import os
import shutil
class KMLBuilder():
  tempfile = open(".tempfile",'w')

  def newKmlFile(this):
    this.tempfile = open(".tempfile",'w')
    this.tempfile.write(KmlHeaders + kmlDocIn + kmlFolderIn)
    this.tempfile.flush()

  def addLineStyle(this, styleID, color, width):
    this.tempfile.write(kmlLineStyleIDIn + str(styleID) + kmlLineStyleIDIn2)
    this.tempfile.write(kmlColorIn + str(color) + kmlColorClose)
    this.tempfile.write(kmlWidthIn + str(width) + kmlWidthClose + kmlLineStyleClose)
    this.tempfile.flush()

  def addPlacemark(this, PlacemarkID, desc, styleID, fromCoord, toCoord):
    this.tempfile.write(kmlPlaceIn + kmlPlaceNameIn + str(PlacemarkID) + kmlPlaceNameClose)
    this.tempfile.write(kmlPlaceDescIn + str(desc) + kmlPlaceDescClose)
    this.tempfile.write(kmlPlaceStyleIdIn + str(styleID) + kmlPlaceStyleIdClose)
    this.tempfile.write(kmlPlaceLineStringIn + kmlCoordIn)
    this.tempfile.write(str(fromCoord[0]) + "," + str(fromCoord[1]) + "," + str(fromCoord[2]) + "\n")
    this.tempfile.write(str(toCoord[0])   + "," + str(toCoord[1])   + "," + str(toCoord[2])   + "\n")
    this.tempfile.write(kmlCoordClose + kmlLineStringClose + kmlPlaceClose)
    this.tempfile.flush()

  def finalize(this, filename):
    this.tempfile.write(kmlFolderClose + kmlDocClose + kmlClose)
    this.tempfile.flush()
    this.tempfile.close()
    shutil.copyfile(".tempfile", str(filename) + ".kml")
    os.remove(".tempfile")



asd = KMLBuilder()

asd.newKmlFile()
asd.addLineStyle("lol", "color", "woot")
asd.finalize("lol")
