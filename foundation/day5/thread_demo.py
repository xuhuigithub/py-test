#!/bin/env python
#coding:utf-8
#当运行这个程序时创建了一个主进程带有一个主线程，主线程又创造了一个子线程去执行函数Foo
#子线程的最大存活时间不超过主线程的最大存活时间，也就是说当主线程销毁时子线程也就没有了，不管子线程是否设置在后台运行

from threading import Thread
import time
def Foo(arg):
  print "%s \n"%(arg)
  for i in xrange(20):
    print i
    time.sleep(1)


print 'before'
t1 = Thread(target=Foo,kwargs={'arg':'xuhui',})
print t1.isDaemon()
#t1.setDaemon(True)
#将子线程发到后台去执行，变为守护线程
t1.start()
#t1.join()
#join方法会阻塞主进程，直到子进程处理完毕，处理子进程时可以设置超时时间，默认为None无限制
print t1.getName()
time.sleep(10)
print 'after'
print '还会阻塞吗'
#time.sleep(10)
#将主进程阻塞住10秒保证其不退出，子进程就不会结束

#time.sleep 会阻塞住主进程
#time.start 也会阻塞主进程
#子进程可以在主进程阻塞时执行
#进程的join方法也会阻塞主进程
