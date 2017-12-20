#!/usr/bin/env python
#encoding: utf-8
"""
生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据:

mygenerator = (x*x for x in range(3))
for i in mygenerator :
...    print(i)
0
1
4
看起来除了把 [] 换成 () 外没什么不同。但是，你不可以再次使用 for i in mygenerator , 因为生成器只能被迭代一次：先计算出0，然后继续计算1，然后计算4，一个跟一个的…
[] 返回的是一个列表
（）返回的是一个生成器

注意生成器只能被迭代一次

"""

def main(max):
  i = 0
  while i < max:
    i += 1
    yield i


if __name__ == '__main__':
  for i in main(4):
   print i