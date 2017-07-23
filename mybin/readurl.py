#!/bin/python
#!_*_conding:UTF-8_*_
import os
import json
import commands

r=os.popen('ls').read().split()
u=open('user.txt','r').read().split()
#r=open('url.txt','r').read().split()
devices=[]
#list
users=[]
a = 0
for device in r:
		user = u[a]
		#str
		devices += [{'{#SITENAME}':device,'{#user}':user}]
		#type dict
		a+=1
print json.dumps({'data':devices},sort_keys=True,indent=7,separators=(',',':'))
#sort_keys	sort

#print devices
