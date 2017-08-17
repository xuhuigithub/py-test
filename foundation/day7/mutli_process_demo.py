#!/usr/bin/env python
#encoding: utf-8
demo_list = [1,2,3,4,5]
from multiprocessing import Pool
import time
def f(x):
  time.sleep(1)
  return x*x

if __name__ == "__main__":
  print map(lambda x:x*x,demo_list),2
  p=Pool(5)
  #最多并发的进程
  #print p.map(lambda x:x*x,demo_list)
  #类似于map函数,但直接使用lambda会报错
  print p.map(f, demo_list),1