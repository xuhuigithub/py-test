#coding:utf-8
def Func2(arg):
  print arg,"Func2"
def wrapper(fun):
  def outer(arg):
    Func2(arg)
    fun(arg)
  return outer

@wrapper
#使这个函数与装饰器关联
def Func1(arg):
  print "Func1",arg


Func1('xuhui')
