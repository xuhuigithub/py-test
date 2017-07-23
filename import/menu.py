#!/bin/env python
import os
import sys
#import paramiko
user = "gsinfo"
hostlist = ['192.168.1.1','192.168.1.2']
applist = ["dedicated-line","dedicated-web"]
def menu(num,menu_list):
  list_tmp = []
  for i in menu_list:
     num += 1
     list_tmp.append("%s    %s"%(num,i))
  menu = "\r\n".join(list_tmp)
  return menu

def chose(menu_list,prompt):
  chosed = []
  menu_chosed = 0
  chose_menu = menu(-1,menu_list)
  while menu_chosed == 0:
    print chose_menu
    chosed_num = raw_input('%s\n'%(prompt)).strip().split()
    for i in chosed_num:
      chosed += [menu_list[int(i)]]
    if len(chosed) > 0:
      menu_chosed = 1
  return chosed


chosed_host = chose(hostlist,'Pls chose host')
chosed_app = chose(applist,'Pls chose app')

print chosed_host,chosed_app

