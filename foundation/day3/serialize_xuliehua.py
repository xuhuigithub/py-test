#!/bin/env python
#coding:utf-8
import pickle
'''
demodata = [1,3,4,6,'xuhui','hehe']
dumpsed = pickle.dumps(demodata, protocol=None)
print dumpsed
print type(dumpsed)
#将对象序列化成字符串
loadsed = pickle.loads(dumpsed)
#反序列化字符串
print loadsed

with open('./testfile') as f:
  filedumps = pickle.dumps(f)
  print filedumps
'''
demodata = [1,3,4,6,'xuhui','hehe']

dumped = pickle.dump(demodata,open('./testfile','w'), protocol=None)
#将序列化后的字符串存入文件
#用处:将内存中的数据dump到硬盘上
with open('./testfile','r') as f:
  print f.read()
loaded = pickle.load(open('./testfile','r'))
#从文件读取数据进行反序列化
print loaded
