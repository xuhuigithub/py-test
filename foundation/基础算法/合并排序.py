#!/bin/env python
#coding:utf-8

B = [1,2,3,25,71]
C = [1,2,25,712]

i = 0       # B的记位变量
j = 0       # C的记位变量
k = 0
A = list()
while i < len(B) and j < len(C):
    if B[i] <= C[j]:
        A.append(B[i])
        i += 1
    else:
        A.append(C[j])
        j += 1

if i == len(B):         #如果i=len(B)那就说明B循环完了，就把剩下的C(C的记位变量以后的值)加进去
    A.extend(C[j:])
else:
    A.extend(B[i:])


print A