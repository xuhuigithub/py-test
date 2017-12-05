#!/bin/env python
#coding:utf-8
def search(sequence,number,lower=0,upper=None):
    if upper is None: upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2   #逐渐缩小upper的值，也就是缩小查找sequence的范围
        if number > sequence[middle]:       #如果数字大于序列中间的数值
            return search(sequence,number,middle+1,upper)   #那就查找中间的右半部分
        else:
            return search(sequence,number,lower,middle) #要不就查找中间的左半部分
class test():
    def __init__(self):
        pass

if __name__ == '__main__':
    seq = [1,3,46,78,88,90,455,64]
    print seq
    print search(sequence=seq,number=88)
    test = test()