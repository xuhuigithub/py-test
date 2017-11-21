#!/usr/bin/env python
#encoding: utf-8

from parse_demo import tree
root = tree.getroot()


demo_country = root[0]
demo_country.set('updated','yes') #set一个属性
rank = demo_country.find('rank')
rank.text = str(1005) #修改一个值
tree.write('output.xml')
