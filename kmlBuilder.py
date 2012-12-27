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
    this.tempfile.write(kmlLineStyleIDIn + styleID + kmlLineStyleIDIn2)
    this.tempfile.write(kmlColorIn + color + kmlColorClose)
    this.tempfile.write(kmlWidthIn + width + kmlWidthClose + kmlLineStyleClose)
    this.tempfile.flush()

  def addPlacemark(this, PlacemarkID, desc, styleID, fromCoord, toCoord):
    this.tempfile.write(kmlPlaceIn + kmlPlaceNameIn + PlacemarkID + kmlPlaceNameClose)
    this.tempfile.write(kmlPlaceDescIn + desc + kmlPlaceDescClose)
    this.tempfile.write(kmlPlaceStyleIdIn + styleID + kmlPlaceStyleIdClose)
    this.tempfile.write(kmlPlaceLineStringIn + kmlCoordIn)
    this.tempfile.write(fromCoord[0] + "," + fromCoord[1] + "," + fromCoord[2] + "\n")
    this.tempfile.write(toCoord[0]   + "," + toCoord[1]   + "," + toCoord[2]   + "\n")
    this.tempfile.write(kmlLineStringClose + kmlPlaceClose)
    this.tempfile.flush()

  def finalize(this, filename):
    this.tempfile.write(kmlFolderClose + kmlDocClose + kmlClose)
    this.tempfile.flush()
    this.tempfile.close()
    shutil.copyfile(".tempfile", filename + ".kml")
    os.remove(".tempfile")


asd = KMLBuilder()

asd.newKmlFile()
asd.addLineStyle("lol", "color", "woot")
asd.finalize("lol")
