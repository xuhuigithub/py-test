#!/bin/env python
#coding:utf-8
'''
所有的类继承于object类
新式类和经典类的区别：
在继承多个父类的情况下 一个是深度优先 一个是广度优先



class Father(object):
  #类如果继承了object 则叫做新式类
  def __init__(self):
    self.note = "这是父类的note"
  def Ffeature(self):
    print "父类特性",self.note

#子类或者叫做派生类
class Son(Father):#括号中写要继承的父类
  #不继承object 则叫做经典类
  def __init__(self):
    self.note = "这是子类的note"
    super(Son,self).__init__()
    #super 函数调用父类的构造函数，父类必须继承object
  def Sfeature(self):
    print "这是子类特性"

  #父类重写
  def Ffeature(self):
    Father.Ffeature(self)
    print "我重写了我的父类，并加上了这句话"
    
Son().Sfeature()
Son().Ffeature()
'''

'''
经典类在继承多个时深度优先
下边例子中 class D 继承了class B和C 而B和C又继承了 class A，当
class D调用save函数时，class B没有则去找到class A 如果class A
也没有则才去寻找class C

新式类则不是，新式寻找父类的方法是广度优先，所以在调用 save函数时 class D 找到了 class C
'''
'''
#经典class A
class A:
  def __init__(self):
    print 'This is A'
  def save(self):
    print 'Save method from A'
'''
#新式class A
class A(object):
  def __init__(self):
    print 'This is A'
  def save(self):
    print 'Save method from A'


class B(A):
  def __init__(self):
    print 'This is B'

class C(A):
  def __init__(self):
    print 'This is C'
  def save(self):
    print 'Save method from __C__'

#class D(C,B):
class D(B,C):
  def __init__(self):
    print 'This is D'
    
c = D()
c.save()
#当class D(C,B): 时执行结果为Save method from __C__，因为是从左到右去继承的
#当class D(B,C): 时执行结果则为Save method from A