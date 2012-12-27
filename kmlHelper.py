#!/usr/bin/python3
#TODO: Remove whitespaces from the variables after stuff works, saves space...?
# why do I have this urge to make every function and class and filename as some sort of monkey
# maybe its because of this file...
KmlHeaders = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
"""
kmlDocIn = """  <Document>
    <name>Travel path</name>
    <open>1</open>
    <description>Generated from gps data</description>
"""
kmlFolderIn = """    <Folder>
      <name>Paths</name>
      <visibility>1</visibility>
      <description></description>
"""

kmlLineStyleIDIn = """      <Style id=" """
kmlLineStyleIDIn2 = """">
        <LineStyle>
"""
kmlColorIn = """          <color>"""
kmlColorClose = """</color>
"""
kmlWidthIn = """          <width>"""
kmlWidthClose = """</width>
"""

kmlLineStyleClose = """        </LineStyle>
      </Style>
"""

kmlPlaceIn = """      <Placemark>
"""
kmlPlaceNameIn = """        <name>"""
kmlPlaceNameClose = """</name>
"""
kmlPlaceDescIn = """        <description>"""
kmlPlaceDescClose = """</description>
"""
kmlPlaceStyleIdIn = """        <styleUrl>"""
kmlPlaceStyleIdclose = """</styleUrl>
"""
kmlPlaceLineStringIn = """        <LineString>
          <extrude>1</extrude>
          <tessellate>1</tessellate>
          <altitudeMode>absolute</altitudeMode>
"""
kmlCoordIn = """          <coordinates>"""

kmlCoordClose = """          </coordinates>
"""
kmlLineStringClose = """        </LineString>
"""
kmlPlaceClose = """      </Placemark>
"""
kmlFolderClose = """    </Folder>
"""
kmlDocClose = """  </Document>
"""
kmlClose = """</kml>
"""
#print(KmlHeaders+kmlDocIn+kmlFolderIn)