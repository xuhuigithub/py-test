#!/usr/bin/env python
#encoding: utf-8

import xml.etree.ElementTree as ET

tree = ET.parse('demo.xml')

root = tree.getroot()

# 子子孙孙递归查询
# for neighbor in root.iter('neighbor'):
#   print(neighbor.attrib)


# country_Liechtenstein = root[0]
# for neighbor in country_Liechtenstein.iter('neighbor'):
#   print neighbor.get('name)
# 找出Liechtenstein的所有neighbor的名字


# for country in root.findall('country'):
#   # 遍历所有的子节点
#   rank = country.find('rank').text
#   # 第一个找到的节点
#   name = country.get('name')
#   print name,rank

