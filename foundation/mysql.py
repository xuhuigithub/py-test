# -*- coding: utf-8 -*-
import sys
import MySQLdb
#import multiprocessing
reload(sys)
sys.setdefaultencoding('utf8')
conn = MySQLdb.connect(
          host = "192.168.61.84",
          port = 3306,
          user = "xuhui",
          passwd = "xuhui",
          db = "zabbix",
          charset = "utf8"
)
cur = conn.cursor()
cur.execute('select name from actions')
data = cur.fetchall()
data = data[1][0]
print data
#print data[0].encode("utf8")
cur.close()
conn.close()
