# !/usr/bin/env python
# encoding: utf-8
from threading import Thread
from threading import Lock
#普通锁
from threading import RLock
#可重入锁
from threading import BoundedSemaphore
import time
num = 0
'''#没有加锁的线程
def addition():
  time.sleep(1)
  #一个线程阻塞 第二个线程开始工作修改全局变量，所以在没有加锁的情况下会加错
  global num
  num += 1
  print '%s\n' %num
'''

'''#加了锁的程序
def addition():
  time.sleep(1)
  global num
  lock.acquire()#加锁
  #加锁以后的程序，锁只加在有实际操作的时候
  num += 1
  print '%s\n' %num
  lock.release()  # 解锁
'''

'''当你的程序需要两把锁时你可以使用这个
rlock = RLock()
def addition():
  time.sleep(1)
  global num
  rlock.acquire()#加锁
  #加锁以后的程序，锁只加载操作的时候
  num += 1
  rlock.acquire()#加锁
  print '%s\n' %num
  rlock.release()   # 解锁
  rlock.release()  # 解锁
'''

def addition():
  global num
  samp.acquire()
  time.sleep(1)
  num += 1
  print '%s\n' %num
  samp.release()

samp = BoundedSemaphore(4)
#设置最多有几个线程可以在这个锁内
#设置最大并发数
lock = Lock()
for i in xrange(5000):
  t = Thread(target=addition,args=())
  t.start()