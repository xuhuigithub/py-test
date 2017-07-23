#coding:utf-8

iterable = [1,2,3,4]
iterable2 = [1,2,3,4,0]
iterable3 = ['']
iterable4 = (1,2,3,4)
iterable5 = ['hehe','haha']
exp = '8*8'
def demo(show):
  print type(show)
'''
#all
all(iterable)
all(iterable2)
all(iterable3)
#获得序列中所有值的bool值为True时返回True，也就是这个序列中不能包含0和空值

#any
any(iterable)
any(iterable2)
any(iterable3)
#遍历序列中所有的值的bool值，任意一个为True则返回真

#max
max(iterable4)
#找出序列中的最大值

#chr
print chr(69),chr(70),chr(71),chr(72)
#返回ASCII码中数字对应的字符

#ord
print ord('E'),ord('F'),ord('G'),ord('H')
#返回ASCII码中对应的数字

#进制转换
print hex(123) #十六进制
print bin(123) #二进制
print oct(123) #八进制

#enumerate
for index,item in enumerate(iterable5):
  print index,item
#返回一个列序列中的索引和值

#字符串的格式化
s = 'I am {0} {1}'
print s.format(*['haha','hehe'])

#执行函数
apply(demo,('1'))
#不能传入数字

#map
map(demo,iterable)
print map(lambda x:x+100,iterable)
#将序列中的每一个元素传入函数并执行

#过滤 
def foo(arg):
  if arg > 1:
    return True
  else:
    return False
print filter(foo,iterable)
#首先定义一个判断的函数如果符合条件则返回True，再将函数和序列放入filter中进行过滤

#reduce
print iterable
print reduce(lambda x,y:x+y,iterable),reduce(lambda x,y:x*y,iterable)
#累加函数，首先序列中的第一个值去和第二个值做运算，假设算出的值为z，那么下一次就是z和第三个值做运算
#如果列表中只有一个值，则默认加0

#zip
print zip(iterable,iterable2,iterable4),zip(iterable,iterable2,iterable3)
#返回的列表中的元组的最大长度为参数序列中最小的那个的长度

#计算字符串
#eval
print eval(exp)
'''




