#!/bin/env python
#coding:utf-8
import time
print time.time()
#时间戳形式
print time.gmtime()
#结构化形式
print time.strftime('%Y-%m-%d %H:%M:%S')
#字符串形式

print time.localtime()
#同样是以结构化形式输出，但是是本地时区的时间

#字符串形式转结构话形式
print time.strptime('2017-07-22','%Y-%m-%d')

#结构化的时间转时间戳的形式
structdemo = time.gmtime()
print time.mktime(structdemo)

#