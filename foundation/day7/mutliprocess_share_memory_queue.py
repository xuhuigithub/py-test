#!/usr/bin/env python
#encoding: utf-8
from multiprocessing import Process,Queue
from Queue import Queue as Queue2

def f(q,n):
  q.put([n,'hello'])

if __name__ == "__main__":
  q = Queue()
  for i in range(5):
    p = Process(target=f,args=(q,i,))
    p.start()
    print q.get()