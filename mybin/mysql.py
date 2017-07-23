# -*- coding: utf-8 -*-
import sys
import MySQLdb
import multiprocessing
reload(sys)
sys.setdefaultencoding('utf8')
ps = 4
class extract_mysql():
  def __init__(self,host,port,user,passwd,db):
    try:
      self.conn = MySQLdb.connect(
          host = host,
          port = port,
          user = user,
          passwd = passwd,
          db = db,
          charset = "gbk"
        )
      self.conncur = self.conn.cursor()
    except Exception as e:
      print 'Mysql conn error \n %s' %(e)
#    finally:
#      if self.conn:
#        self.conn.close()

  def get_tables(self):
    with self.conn:
      self.conncur.execute('show tables')
      tables = self.conncur.fetchall()
      tablelist = []
      for i in xrange(len(tables)):
        tablelist.extend(tables[i])
      return tablelist

  def get_head(self,table):
    with self.conn:
      cur = self.conncur
      cur.execute("select * from %s limit 1"%(table))
      head = cur.description
      columns = []
      for i in xrange(len(head)):
        columns.append(head[i][0])
      columns = ",".join(tuple(columns))
      columns = "(%s)" % columns
      return columns

  def get_data(self,table):
    with self.conn:
        cur = self.conncur
        cur.execute("select * from %s"%(table))
        datas = cur.fetchall()
        datalist = [ x for x in datas ]
        return datalist

  def command_db(self, sql):
    try:
      result = self.conncur.execute(sql)
      self.conn.commit()
      return result
    except Exception as e:
      print e
    finally:
      if self.conn:
        self.conn.close()
  def ps_insert(self,data,part):
    with self.conn:
      queue = len(data)
      step = (queue / ps) + 1
      a = part * step
      b = (part + 1) * step
      if b > queue:
        b = queue
      elif b < queue and part == ps:
        b = queue
      #保证不丢数据
      print a,b
      print len(data[a:b])
      #datas = ",".join(data[a:b])
      datas = data[a:b]
      #数据转换将数据转换为字符串，让sql语句识别
      cur = self.conncur
     # sql = "insert into %s values %s" %(table,datas)
      sql = 'insert into actions values(%s,%s,%s,%s)'
      print sql
      cur.executemany(sql,datas)
      self.conn.commit()



try:
  conn = extract_mysql('192.168.61.84',3306,'xuhui','xuhui','zabbix')
  conn2 = extract_mysql('192.168.100.150',3306,'xuhui','xuhui','zabbix')
  datas = conn.get_data('actions')
  print datas
  conn2.ps_insert(datas,1)


#  datas2 = conn2.get_data('actions')
#  print datas
#  conn2.ps_insert('actions',datas,1)
#  print datas
#  tables = conn2.get_tables()
#  pool = multiprocessing.Pool(processes=ps)
#  for i in xrange(0, ps+1):
#    pool.apply_async(target=conn2.ps_insert('actions', datas, i))
 #   conn2.ps_insert('actions', datas, i)
#  pool.colse()
#  pool.join()

#  print datas
#  columns = conn.get_head('actions')
#  print
#  testdata = [('1','xuhui'),('2','hehe')]
#  conn2.insert_more('test',testdata)
#  datas = ('1', 'Report not supported items', '3', '0', '1', '3600', '{ITEM.STATE}: {HOST.NAME}:{ITEM.NAME}', 'Host: {HOST.NAME}\r\nItem: {ITEM.NAME}\r\nKey: {ITEM.KEY}\r\nState: {ITEM.STATE}', '1', '{ITEM.STATE}: {HOST.NAME}:{ITEM.NAME}', 'Host: {HOST.NAME}\r\nItem: {ITEM.NAME}\r\nKey: {ITEM.KEY}\r\nState: {ITEM.STATE}', '')
#  datas = "(%s)" %(datas)
#  print datas
#  print columns
  #print datas[1],columns
#  conn2.command_db('insert into actions %s VALUES %s'%(columns,datas[1]))
  #for i in xrange(len(datas)):
#  conn2.command_db("insert into actions %s values %s" %(columns,datas[i]))
#  conn2.command_db('insert into actions ()')
#  columns = conn.get_head('actions')
#  datas = conn.get_data('actions')
#  print datas
#  for i in xrange(len(datas)):
#    print datas[i]
except Exception as e:
  print e

  #  tablesql = "show tables"
  #  tables = conn.command_db(tablesql)
  #
  #
  #
  #   print tablelist