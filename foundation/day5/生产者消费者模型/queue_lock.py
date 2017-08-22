#!/usr/bin/env python
#encoding: utf-8
import Queue
from threading import Thread
import time
q = Queue.Queue()

def demo_que(n):
  q.put(n)
  print '第%s次' %n
  time.sleep(3)
  #如果队列没有锁的话，那么在sleep时，别的线程应该可以去操作队列
  #但结果显示队列是有锁的
  print q.get()

for i in xrange(5):
  p = Thread(target=demo_que,args=(i,))
  p.start()
  p.join()