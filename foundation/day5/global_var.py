# !/usr/bin/env python
# encoding: utf-8
num = 0
def addition():
  global num
  #不能在局部内修改全局变量，如果想要修改必须先声明global
  num += 1
  print num

addition()
print num