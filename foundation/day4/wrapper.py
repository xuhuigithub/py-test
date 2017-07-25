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

#加载函数到内存
#发现有需要装饰的函数 (wrapper（@）标志的函数)
#进行wrpper 将函数重新赋值（复制成装饰器内部的函数）
#在执行装饰过的函数时 想往常执行函数一样执行