#!/bin/env python
#coding:utf-8
#父类或者叫做基类
class Father:
  def __init__(self):
    self.note = "这是父类的note"
  def Ffeature(self):
    print "父类特性",self.note

#子类或者叫做派生类
class Son(Father):#括号中写要继承的父类
  def __init__(self):
    self.note = "这是子类的note"
    
  def Sfeature(self):
    print "这是子类特性"

  #父类重写
  def Ffeature(self):
    Father.Ffeature(self)
    print "我重写了我的父类，并加上了这句话"
    
Son().Sfeature()
Son().Ffeature()
#子类将方法从父类继承了过来，但是动态字段用的还是子类的
#这个动态字段也可以被修改，例如从父类继承来__init__()函数
#Father.__init__(self)  
