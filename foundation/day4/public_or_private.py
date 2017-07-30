#!/usr/bin/env python
#coding:utf-8
class person(object):
#类必须继承object 才有只读，只写字段,默认是可以读可以写的
#类必须去继承object 才能修改私有字段
  def __init__(self,flag,flag2):
    self.__private = flag
    #这是一个私有字段，外部不能直接使用
    self.public = flag2

  def show(self):
    print self.__private
    #内部可以调用私有字段

  def __private_method(self):
    return "这是一个私有方法，外部不能调用我"
    #这是一个私有方法，外部不能直接使用


  @property
  #访问私有方法还可以这样
  #修改私有字段的值：推荐去调用@property装饰器，只有这个装饰器才可以使用setter属性
  def private_show(self):
    return self.__private

  def private_show_n(self):
    return self.__private
  #如果你非得调用内部方法的话 可以实例化一个对象再调用这个方法
  #做一个测试看看setter能不能修改普通的动态方法,答案是不能访问

  @staticmethod
  def static_func():
    print "xxxxx"
 
  @private_show.setter
 #只能修改经过装饰器@property装饰过的方法
 #修改私有字段的装饰器
  def modify_private_show(self,value):
    self.__private = value

people = person('xuhui','hehe')
try:
  print people.__private
except AttributeError:
  print """
  print people.__private 错误
  __private 是一个私有字段，所以你并不能直接访问
  但是你可以通过函数调用
  例如people.show()
  """
  people.show()

print people.public
print "普通的动态字段则随便访问 people.public"
print people._person__private_method(),"我就要访问私有方法"

people.__private = "aaa"

person.private_show

people.static_func()

print people.private_show_n()
