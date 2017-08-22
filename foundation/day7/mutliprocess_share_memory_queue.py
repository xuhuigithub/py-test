#!/usr/bin/env python
#encoding: utf-8
from multiprocessing import Process,Queue
# import Queue as Q2

def f(q):
  #为什么不能global，queue呢？
  #每个进程之间不共享内存，你global一次也就是复制一次主进程的queue
  q.put([42,None,'hello'])

if __name__ == "__main__":
  q = Queue()
  #这个queue是主进程的queue
  p = Process(target=f,args=(q,))
  #1、子进程向queue中放入数据
  p.start()
  p.join()
  print q.get()
  #2、父进程拿到数据