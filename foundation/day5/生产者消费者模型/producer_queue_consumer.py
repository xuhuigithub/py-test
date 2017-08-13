#!/bin/env python
#coding:utf-8
#生产者消费者模型
''' 
为什么使用生产者消费者模型？
http://www.cnblogs.com/bizhu/archive/2012/05/17/2506202.html
'''
from threading import Thread
from Queue import Queue
from Queue import Empty
from time import sleep

demo_queue = Queue()

class Producer(Thread):
  def __init__(self,name,queue):
    self.Queue = queue
    self.Name = name
    Thread.__init__(self)
    #super(Producer,self).__init__()
  def run(self):
    while True:
      self.Queue.put('baozi')
      print self.Name,'生产了一个包子'
      sleep(3)
      #为什么加sleep？
      #不加sleep下一个线程永远执行不了
'''

def Producer1(name,queue):
  while True:
    queue.put('baozi')
    print name,'生产了一个包子'
    sleep(3)
chef1 = Thread(target=Producer,args=('chef1',demo_queue,)      
#简单点也可以这样写
'''

class Consumer(Thread):
  def __init__(self,name,queue):
    self.Queue = queue
    self.Name = name
    Thread.__init__(self)
    #super(Producer,self).__init__()
  def run(self):
    while True:
      try:
        self.Queue.get_nowait()
      except Empty:
        print '队列中没有包子了'
        print '我等一会'
        sleep(3)
      else:
        print self.Name,'得到了一个包子'

producer1 = Producer('chef1',queue=demo_queue)
producer1.start()
producer2 = Producer('chef2',queue=demo_queue)
producer2.start()
producer3 = Producer('chef3',queue=demo_queue)
producer3.start()
consumer1 = Consumer('consume1',queue=demo_queue)
consumer1.start()