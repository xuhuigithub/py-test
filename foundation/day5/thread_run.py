#!/bin/env python
#coding:utf-8

#当我们执行一个程序时，其实是调用了run方法来执行

from threading import Thread


class MyThread(Thread):
#   def run(self):
#     print '我是线程'
  def run(self):
    Thread.run(self)
    print '我是线程'

def Demo():
  print "target Function"
t1 = MyThread(target=Demo)
t1.start()