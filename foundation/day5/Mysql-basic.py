# !/usr/bin/env python
# encoding: utf-8

import MySQLdb
from MySQLdb.constants import FIELD_TYPE
my_conv = { FIELD_TYPE.LONG: int,FIELD_TYPE.STRING: list }
'''
conn = MySQLdb.connect(
  host='192.168.100.150',
  user='root',
  passwd='123456',
  db='person',
  port=3306,
  charset='utf8'
)
#数据库 就像一间房子
cur = conn.cursor()
#cur 游标 就像一只手
#就好比进入房子后我们用手去操作

selectsql = 'select * from users'
rCount = cur.execute(selectsql)
#execute 默认返回的是你的sql语句影响了多少行数
data = cur.fetchall()


insertsql = 'insert into users (user_name,user_pass) values(%s,%s)'
#这个百分比s不是字符串的%s的意思，仅仅就是execute方法中的一个占位符，所以不存在什么%d一类的
params = ('xuhui2','123456')
#内容 作为参数传入execute方法中
cur.execute(insertsql,params)
conn.commit()
#在插入请求完成后使用commit方法去提交


deletesql = "delete from users where user_name=%s"
deleteparams = ("xuhui2",)#为什么多了一个逗号？ 声明这个变量是一个序列
delresult = cur.execute(deletesql,deleteparams)
delnotify = "删除成功,删除了%s条数据" %(delresult) if delresult > 0 else "没有这条数据"


updatesql = "update users set user_name=%s where user_id = 1"
updateparams = ("xuhui6",)
upresult = cur.execute(updatesql,updateparams)
#不需要commit 即可更新

conn.rollback()
#回滚操作
cur.close()
conn.close()


print data
print delnotify
'''

'''
import MySQLdb
conn = MySQLdb.connect(
  host='192.168.100.150',
  user='root',
  passwd='123456',
  db='person',
  port=3306,
  charset='utf8'
)


cur = conn.cursor()
#向数据库中批量插入数据
datalist =[
  ("xuhui6","hehe"),
  ("xuhui7","haha"),
]
moreinsert = cur.executemany('insert into users(user_name,user_pass) values(%s,%s)',datalist)
conn.commit()

#将表的列名和数据一并取出
cur =conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
selectsql = 'select * from users'
rCount = cur.execute(selectsql)
data = cur.fetchall()
cur.close()
conn.close()
print data
#返回值样例
# {'user_name': u'xuhui6', 'user_id': 1L, 'user_pass': u'123456'}, {'user_name': u'xuhui7', 'user_id': 22L, 'user_pass': u'haha'}, {'user_name': u'xuhui6', 'user_id': 21L, 'user_pass': u'hehe'}, {'user_name': u'xuhui7', 'user_id': 20L, 'user_pass': u'haha'})
'''


'''
conn = MySQLdb.connect(
  host='192.168.100.150',
  user='root',
  passwd='123456',
  db='person',
  port=3306,
  charset='utf8'
)
#Mysql fetchone

cur = conn.cursor()
cur.execute('select * from users')
data = cur.fetchone()
#每取到一条数据指针向下走一次
print data
data = cur.fetchone()
print data
#第二次取到的数据是第一次的下一条数据

#更改指针位置相对定位和绝对定位
##相对定位
cur = conn.cursor()
cur.execute('select * from users')
data = cur.fetchone()
#每取到一条数据指针向下走一次
print data
cur.scroll(-1,mode='relative')
#相对于现在的指针位置-1
data = cur.fetchone()
print data
##绝对定位
cur.scroll(2,mode='relative')
#指针的位置以正整数或者负数表达
data = cur.fetchone()
print data

cur.scroll(0,mode='absolute')
#将指针放回到起点，最小为-1
data = cur.fetchone()
print data

#获取上一条数据的自增ID
#用处：在做表关联时，将自增ID取出存入与其相关联的表
cur = conn.cursor()
sql = 'insert into users (user_name,user_pass) values(%s,%s)'
params = ('xuhui','1111111',)
cur.execute(sql,params)
conn.commit()
users_id = cur.lastrowid
#获得上一次插入数据的自增ID
print users_id

cur.close()
conn.close()
'''

conn = MySQLdb.connect(
  host='192.168.61.84',
  user='xuhui',
  passwd='xuhui',
  db='zabbix',
  port=3306,
  conv = my_conv,
#  charset = 'utf8'
)
cur = conn.cursor()
cur.execute('select * from actions')
datas = cur.fetchall()
print datas
for i in datas:
  print i
cur.close()
conn.close()
