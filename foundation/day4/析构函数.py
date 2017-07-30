#!/bin/env python
#coding:utf-8
class Foo:
  def __init__(self,note):
    self.note = note
  def __call__(self):
    print "当你使用我生成的对象时我会出现"
  def __del__(self):
    print "生成的对象呗python的垃圾回收器回收了"

demo_object = Foo("生成一个对象")
demo_object()
