#!/bin/env python
#coding:utf-8
def dict_args(**kwargs):
  kwargs2 = kwargs.copy()
  home = kwargs2['home']
  name = kwargs2['name']
  print home
  print name
  
def list_args(*args):
  args2 = args
  home = args2[0]
  name = args2[1]
  print home
  print name

dict_arg = {'home':'shangdi','name':'xuhui'}
dict_args(**dict_arg)
list_arg = ('11','22')
list_args(*list_arg)