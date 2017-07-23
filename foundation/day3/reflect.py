#!/bin/env python
#coding:utf-8
'''
temp = 'sys'
#首先定义一个变量
mode1 = __import__(temp)
#导入模块然后将其赋值给一个变量
print mode1.path

#其实还可以这样做


import sys as mode2
print mode2.path

temp = 'demo'
mode1 = __import__(temp)
mode1.show(2)
newshow = getattr(mode1, 'show')
newshow(2)

#另一种做法

from demo import show as newshow
newshow(2)

'''

