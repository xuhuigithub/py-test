#!/bin/env python
#coding:utf-8
import random
def genpin(lenthy):
  code = []
  for i in xrange(lenthy):
    if i == random.randint(0,lenthy):
      intcode = str(i)
      code.append(intcode)
    else:
      letcode = chr(random.randrange(65,91))
      code.append(letcode)  
  code = ''.join(code)
  return code


if __name__ == "__main__":
  print genpin(6)
    
      
      
    