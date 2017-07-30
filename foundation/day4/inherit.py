#!/bin/env python
#coding:utf-8
#父类或者叫做基类
class Father:
  def __init__(self):
    self.note = "这是一个父类"
  def Ffeature(self):
    print "父类",self.note

#子类或者叫做派生类
class Son(Father):#括号中写要继承的父类
  def __init__(self):
    self.note = "这是一个子类"

  def Sfeature(self):
    print "这是一个子类"

  #父类重写
  def Ffeature(self):
    Father.Ffeature(self)
    print "这是我给我的父类增加的东西"
    
Son().Sfeature()
Son().Ffeature()
#子类将方法从父类继承了过来，但是动态字段用的还是子类的
  
