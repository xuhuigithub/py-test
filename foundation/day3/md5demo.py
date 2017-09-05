#!/bin/env python
#coding:utf-8
import hashlib
import hmac
hashmd5 = hashlib.md5()
hashmd5.update('admin')
#update方法随时可以向加字符串到里边去
print hashmd5.digest()
#以二进制显示
print hashmd5.hexdigest()
#以十六进制显示
temp = hashlib.sha256()
temp.update('admin')
print temp.digest(),temp.hexdigest()
x = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
if x == temp.hexdigest():
  print 'hehe'

secret = hmac.new('secret_key')
secret.update('test message')
message = secret.hexdigest()
print message
#在原有的基础上再加密一层（使用自己生成的Key）