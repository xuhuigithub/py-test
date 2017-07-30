#!/bin/env python
#coding:utf-8
'''
抽象方法加抽象类提供一个规范接口
使用环境：
比如我们可以先用规范接口写出一个规范
例如下边例子中 要求我们的报警要有微信
当我们的类继承了规范接口时我们的方法中就必须要有Weixin函数
'''
from abc import abstractmethod,ABCMeta
class Alert:
  __metaclass__ = ABCMeta
  
  @abstractmethod
  def Weixin(self):pass

class XAlert(Alert):
  def __init__(self):
    print '__init__'
  def Weixin(self):
    print '向接口交付微信方法'
XAlert().Weixin()