#!/bin/env python
#coding:utf-8
import re
'''
result1 = re.match('\d+','adasdcvvaknaaks223asd66as')
if result1:
  print result1.group()
else:
  print result1

result2 = re.search('\d+','adasdcvvaknaaks223asd66as')
print result2.group()

#search 和  match 的区别 
match 是从头开始匹配，如果匹配到了则返回，如果没匹配到则返回None
search 是只要匹配任意一条即可

#findall 寻找整个字符串，将所有着匹配的结果组成列表返回
result3 = re.findall('\d+','adasdcvvaknaaks223asd66as')
print result3

#compile 对正则表达式进行编译，其实上边的所有re都是先对正则表达式进行编译然后在执行的
regnum = re.compile('\d+')
result4 = regnum.findall('adasdcvvaknaaks223asd66as')
print result4

'''
#groups 返回的格式为元组 结果：('456', 'aa')
result5 = re.search('([1-9]{3})(a{2})','456aa')
#首先re.search 应用正则[1-3]{3} 将456匹配到，再应用正则a{2}将aa匹配到
if result5:
  print result5.groups()
else:
  print 'fail'  
