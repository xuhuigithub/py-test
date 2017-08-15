# !/usr/bin/env python
# encoding: utf-8
import threading
import time
event = threading.Event()

#event.wait()阻塞进程
#同一个进程内存空间内的线程在event.wait()后，event.set()后才能释放(线程共享同一块内存空间)
#在set后需要再次event.clear() 重置event.wait()
def seter():
  time.sleep(3)
  event.set()
  print '我执行完了并将wait设置为了True'
def waiter():
  event.wait()
  print '我将执行seter之后的动作'
  #阻塞时另一个线程就会执行

waiter_instance = threading.Thread(target=waiter)
seter_instance = threading.Thread(target=seter)
waiter_instance.start()
seter_instance.start()