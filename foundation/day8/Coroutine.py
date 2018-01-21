#!/usr/bin/env python
# encoding: utf-8
# 协程
def consumer():
    r = 0
    while True:
        n = yield r #第一次send(None)到这里,返回r的初始值0,并暂停(pause),当第二次send(1)到这里时赋值1给n 从上次暂停的位置继续执行，然后返回r，再次循环第一次send()过来的步骤（返回值，并且暂停）
        #参考：http://blog.csdn.net/soonfly/article/details/78361819
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'    #这个值将会在yield r 处返回（当start generator后）


def produce(c):
    c.send(None)    #can't send non-None value to a just-started generator
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)

"""
执行流程： 
1、通过c.send(None)或者next(g)启动生成器函数，并执行到第一个yield语句结束的位置。这里是关键，很多人就是在这里搞糊涂的。运行receive=yield value语句时，我们按照开始说的拆开来看，实际程序只执行了1，2两步，程序返回了value值，并暂停(pause)，并没有执行第3步给receive赋值。因此yield value会输出初始值' '。这里要特别注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。

2、通过c.send('1')，会传入1，从上次暂停的位置继续执行，那么就是运行第3步，赋值给receive。然后计算出value的值，并回到while头部，遇到yield value，程序再次执行了1，2两步，程序返回了value值，并暂停(pause)。此时yield value会输出1，并等待send()激活。

3、通过g.send(123456)，会重复第2步，最后输出结果为”got: 123456″。

4、当我们g.send(‘e’)时，程序会执行break然后推出循环，最后整个函数执行完毕，所以会得到StopIteration异常。

从上面可以看出， 在第一次send(None)启动生成器（执行1–>2，通常第一次返回的值没有什么用）之后，对于外部的每一次send()，生成器的实际在循环中的运行顺序是3–>1–>2，也就是先获取值，然后dosomething，然后返回一个值，再暂停等待。
"""