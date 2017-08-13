#!/bin/env python
#coding:utf-8
from Queue import Queue
demo_queue = Queue(maxsize=100)
from Queue import Empty
'''
#生成一个队列最大长度为100
demo_dict = {"name":"xuhui"}
demo_list = ['1',1,2,3]
demo_tuple = (1,2,'3')
demo_queue.put(demo_dict)
demo_queue.put(demo_list)
demo_queue.put(demo_tuple)

print demo_queue.qsize()

print demo_queue.get()
print demo_queue.get()
print demo_queue.get()

秉承着先进先出的原则第一个get到的也就是第一个put的
上边执行的结果是
3
{'name': 'xuhui'}
['1', 1, 2, 3]
(1, 2, '3')
'''
'''
demo_queue.put(u'demo')
if demo_queue.empty():
  print '队列是空的'
else:
  print '队列不是空的'

if demo_queue.full():
  print '队列是满的'
else:
  print '队列不是满的'

demo_queue.get()
#demo_queue.get(timeout=1)
#如果队列中没有数据时再去get的话会阻塞程序，当然也可以设置超时时间,时间过后自动抛出异常
#或者使用nowait
try:
  print demo_queue.get_nowait()#如果没有可以get的数据则抛出异常
except Empty:
  print "队列是空的了"

'''
'''
with open('./test','r') as f:
  demo_queue.put(f)
  print demo_queue.get().read()
'''