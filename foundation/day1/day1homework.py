#!/bin/env python
import sys
#fail = 0
file = 'user.lock'
f = open(file,'a')
f.close()
f = open(file,'r')
#if fail == 3:
#	print 'login lock'
#else:
login = "0"
for fail in range(0,3):
#while fail < 3:
	username = "" 
	password = ""
	while username == '' and login == "0":
		username = raw_input('Pls input your username:').strip()
		if username == "":
			print "username can't be empty "
			continue
		elif username in f.read():
			print "user is locked"
			sys.exit()
	while password == '' and login == "0":
		password = raw_input('Pls input you password:').strip()
		if password == "":
			print "password can't be empty "
			continue
		if username == 'xuhui' and  password == '123456':
			f.close()
			print 'login successful'
			login = '1'
			break
		else:
			print 'username or password incorrect'
else:
	if fail == 2 and login == "0":
		f.close()
		print 'login lock' 
		f = open(file,'a') 
		f.write(username)
		f.close()
