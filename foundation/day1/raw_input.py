#!/bin/env python
#_*_conding:UTF-8_*_
name = raw_input("Pls input your name:")
old = raw_input("Pls input your old:")
address = raw_input("Pls input your address:")
msg = """
Infotmation of %s
name:\033[31;1m%s \033[0m
old:%s
address:%s
"""%(name,name,old,address)
if int(old) >= 50:
	print "max"
elif int(old) >=30:
	print "middle"
else:
	print "min"
print msg
