#!/usr/bin/env python
#encoding: utf-8

import xml.etree.ElementTree as ET
root = ET.Element('NACAOREQUEST')
username = ET.SubElement(root,'USERNAME')
password = ET.SubElement(root,'PASSWORD')
cainfo = ET.SubElement(root,'CAINFO')
interfaceinfo = ET.SubElement(root,'interfaceinfo'.upper())
code = ET.SubElement(interfaceinfo,'code'.upper())
param1 = ET.SubElement(interfaceinfo,'param1'.upper())

print ET.dump(root)