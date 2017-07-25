#coding:utf-8


def Filter_before(request,kargs):
  print "I'm before"

def Filter_after(request,kargs):
  print "I'm after"

def Filter(before_func,after_func):
  def outer(main_func):
    def wrapper(request,kargs):
      before_result = before_func(request,kargs)
      if before_result != None:
        return before_result

      main_result =  main_func(request,kargs)
      if main_result != None:
        return main_result
        #当没有返回值时不会报错

      after_result = after_func(request,kargs)
      if after_result != None:
        return  after_result

    return wrapper
  return outer

@Filter(Filter_before,Filter_after)
def List(request,kargs):
  return "I'm main"

print List(1,2)