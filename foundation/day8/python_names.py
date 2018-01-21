#!/usr/bin/env python
# encoding: utf-8
"""
Python 中一切皆为对象，数字是对象，列表是对象，函数也是对象，任何东西都是对象。
而变量是对象的一个引用（又称为名字或者标签），对象的操作都是通过引用来完成的。
例如，[]是一个空列表对象，变量 a 是该对象的一个引用
ref: https://foofish.net/python-function-args.html
#！ 参考：http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#default-parameter-values
"""

"""
重点：变量是对象的一个引用
"""
a = 1
# 1是对象 而a是对1这个对象的引用（也可以叫做打标签）
a = 2
# 就是把原来对象1身上的a标签放到了对象2身上


def bad_append(newitem,alist=[]):       #这个alist的默认绑定的对象是在函数被定义时就生成的[]
    #这里把alist标签挂在了一个list对象上
    alist.append(newitem)
    return alist
#后续的就不会变了吗？


def good_append(newitem,alist=None):
    #这里把alist标签挂在了一个list对象上
    if alist is None:
        alist = []
        alist.append(newitem)       #这个alist是在函数被调用时才生成的(good_append())
    return alist
