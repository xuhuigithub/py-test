#coding:utf-8


def Filter_before(request,kargs):
#7、Filter_before经过装饰的函数执行的第一个函数
  return "I'm before"

def Filter_after(request,kargs):
  return "I'm after"

def Filter(before_func,after_func):
#3、为wrapper函数添加参数
  def outer(main_func):
#4、加载outer函数到内存中，并且确定要wrapper的函数
    def wrapper(request,kargs):
#5、加载wrapper函数到内存中 返回真正的wrapper，也就是最后要装饰的函数是等于它的
      before_result = before_func(request,kargs)
#6、按顺序执行函数内部代码最后返回结果
      if before_result != None:
        return before_result

      main_result =  main_func(request,kargs)
      if main_result != None:
        return main_result
        #当有返回值时直接返回退出，也可以不这样写，这个程序的目的是在一个已经写好的函数前边和后边毫不费力的执行另外两个函数

      after_result = after_func(request,kargs)
      if after_result != None:
        return  after_result

    return wrapper
  return outer

@Filter(Filter_before,Filter_after)
#2、程序执行到@Filter(Filter_before,Filter_after)时 检测到wrapper返回到上层wrapper函数处，并传参(Filter_before,Filter_after)

def List(request,kargs):
  pass


print List(1,2)
#1、同样的首先是加载函数到内存
#2、程序执行到@Filter(Filter_before,Filter_after)时 检测到wrapper返回到上层wrapper函数处，并传参(Filter_before,Filter_after)
#3、为wrapper函数添加参数
#4、加载outer函数到内存中，并且确定要wrapper的函数
'''
#5、加载wrapper函数到内存中 返回真正的装饰器{wrapper(request,kargs)函数}，也就是要装饰的函数是等于它的也就是List(request,kargs)= wrapper(request,kargs): 
                                                                                                                          before_result = before_func(request,kargs)
                                                                                                                          .........
                                                                                                                          .....
'''
#6、按顺序执行经过装饰后的函数内部代码最后返回结果