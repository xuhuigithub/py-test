#coding:utf-8
'''
把省分为一类，所有的省都有如下特点
name 都有名子
capital 都有省会
leader 都有领导人

通过类实例化创建了一个对象（省）
'''

class Province:
  #一个类
  @staticmethod
  def Foo():
    print "每个省要带头反腐"
  #静态方法

  memo = "中国的23个省之一"
  #静态字段
  #属于类

  def __init__(self,name,capital,leader):
    self.name = name
    #动态字段
    #属于对象
    self.capital = capital
    self.leader = leader
    Province.Foo()
    #同样的每个对象也可已访问静态方法



  def sports_meet(self):
    #动态方法
    #这是一个方法，提供给对象调用
    print self.name + "正在开运动会"



hb = Province('河北','石家庄','我自己')
sd = Province('山东','济南','我自己')
#Province 是一个类，类实例化后创建一个对象，hb就是一个对象
print hb.name
print Province.memo
Province.memo = "hehe"
#可以修改静态字段
print Province.memo

sd.sports_meet()

Province.Foo()