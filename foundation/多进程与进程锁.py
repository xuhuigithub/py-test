#!/bin/env python
#coding:utf-8

from multiprocessing import Pool,cpu_count
from threading import Lock
import time
import requests
import os
import random
lock = Lock()
file = 'testfile.txt'
def func(x):
  # requests.get('http://www.baidu.com').text
  # map会把进程准备好，而requests这个谁先跑完谁拿到锁，然后写，所以会导致乱序
  with lock:
    # time.sleep(random.randint(1,5))
    # #不要在锁中加入这种时间复杂度没有一定值的代码

    with open(file,'ab') as f:
      f.write(str(x))
  return x


if __name__ == "__main__":
  for i in xrange(1,10):
    p = Pool(processes=cpu_count())
    # print (p.map(func,[1,2,'3\n']))
    # 和map函数是一样的效果最后返回的是一个列表
    for x in [1,2,'3\n']:
      p.apply_async(func=func,args=(x,))
    p.close()
    p.join()
