#!/usr/bin/env python
#encoding: utf-8
import os
from multiprocessing import Process
#Process方法与Thread方法类似
def info(title):
  print title
  print 'module name: %s' %__name__
  if hasattr(os,'getppid'):
    print 'parent process:',os.getppid()
  print 'process id:',os.getpid()

p1 = Process(target=info,args=('hehe',))
p1.start()
p1.join()
#默认的多进程是fork方法，父进程派生子进程