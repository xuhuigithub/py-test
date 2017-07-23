#!/bin/env python
#coding:utf-8
import json
'''
demo_dict = {'name':'xuhui','age':12}
dumpsed = json.dumps(demo_dict)
print dumpsed,type(dumpsed)
loadsed = json.loads(dumpsed)
print loadsed,type(loadsed)
if loadsed['name'] == 'xuhui':
  print loadsed['age']
'''
demo_dict = {'name':'xuhui','age':12}
with open('./testfile','w') as f:
  dumped = json.dump(demo_dict,f)
with open('./testfile','r') as e:
  loaded = json.load(e)
  print loaded