#!/bin/env python
for i in range(10):
	if i == 5:
		print "i=%s" %(i)
		continue
	elif i >= 7:
		break
	print i
