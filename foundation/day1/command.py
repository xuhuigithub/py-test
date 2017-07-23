#!/bin/env python
#_*_conding:UTF-8_*_
import commands
status,output=commands.getstatusoutput('ls')
print 'status:'+str(status)+''
print 'stdinoutput:\n'+output+''
