# !/usr/bin/env python
# encoding: utf-8'
from homework import person_action

def befor_walk(people):
  person_action.shit(people)

def after_walk(people,after):
  person_action.shit(people)

def people_walk(before_func,after_func):
  def outer(main_func):
    def wrapper(*args, **kw):
      before_func('xuhui')
      main_func(*args)
      after_func('xuhui',after='2')
    return wrapper
  return outer

class Person(object):
  def __init__(self,name,gender,gene,habit,muscle=0):
    self.name = name
    self.gender = gender
    self.__gene = gene
    self.habit = habit
    self.muscle = muscle
  @people_walk(befor_walk,after_walk)
  def walk(self):
    print self.name,'walk'
    self.muscle += 1
    print "Now your muscle has been improve,%s" %(self.muscle)

  def talk(self,msg):
    print "%s say %s" %(self.name,msg)
  @property
  def see_gene(self):
    print self.__gene
  @staticmethod
  def drink_bee():
    print "cheers"


xuhui = Person('xuhui','man','good','hehe',100)
xuhui.walk()



