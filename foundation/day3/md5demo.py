#!/bin/env python
#coding:utf-8
import hashlib
hashmd5 = hashlib.md5()
hashmd5.update('admin')
print hashmd5.digest()
#以十六进制显示
print hashmd5.hexdigest()

temp = hashlib.sha256()
temp.update('admin')
print temp.digest(),temp.hexdigest()
x = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
if x == temp.hexdigest():
  print 'hehe'