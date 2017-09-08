#!/usr/bin/env python
#encoding: utf-8
#需求：在所有以实现功能的函数上加上验证功能（在不修改原有代码的情况下）



# def welcome():
#   print 'Hello xuhui'

#以前执行函数是这样的：welcome(),在加完功能后要求继续可以这样调用

# print welcome
#在不加括号执行函数时 会返回函数的内存地址，而不会执行函数

# #第一种方法 原理：将原函数的内存地址放到验证函数中去，在执行welcome = varfiy(welcome)时首先执行验证函数内部的代码，然后返回原函数的内存地址，再交给变量
#出现的问题：在程序每次执行welcome = varfiy(welcome)时都会先去执行 验证函数print '这是验证要用的代码'，即使不执行最后要执行的welcome函数
# def varify(func):
#   print '这是验证要用的代码'
#   return func
# def welcome():
#   print 'Hello xuhui'
# welcome = varify(welcome)
# welcome()

#第二种方法直接使用Python内部提供的装饰器
# def varify(func):
#   def inner(arg):   #arg代指包装函数的参数
#     print '这是验证要用的代码'
#     return func(arg)
#   return inner
#
# @varify
# def welcome(name):
#   print 'Hello %s' %name
#
# welcome('xuhui')

#复杂用法，被装饰的函数需要数量不同的参数
def varify(func):
  def inner(*args):   #arg代指包装函数的参数
    print '这是验证要用的代码'
    return func(*args)
  return inner

@varify
def welcome(name):
  print 'Hello %s' %name

@varify
def go(name,passwd):
  print 'Hello %s PASS: %s' %(name,passwd)
welcome('xuhui')
go('xuhui','123456')