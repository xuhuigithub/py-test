#!/bin/env python
#coding:utf-8

class rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width,self.height
    size = property(fget=getSize,fset=setSize)
    #property ，主要用于很方便的修改对象的变量，详见property的doc
if __name__ == '__main__':
    # print property.__doc__
    r = rectangle()
    r.size = (12,2)    #等于r.setSize((12,2))  r.width=12 r.height=2  修改内部变量是不是很方便
    print r.size        #等于 r.getSize()