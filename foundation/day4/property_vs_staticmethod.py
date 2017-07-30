#!/bin/env python
#coding:utf-8
class demo_class:
  def __init__(self,note):
    self.note = note
  @staticmethod
  def static_method():
    print "静态方法无法使用对象的变量(self.*),因此我无需实例化也可以被执行"
  @property
  def property_attribute(self):
    print self.note,"特性可以使用对象的变量"

demo_object = demo_class('调用我时不用加括号哦，因为我是一个特性')
demo_class.static_method()
demo_object.property_attribute
