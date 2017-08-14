# !/usr/bin/env python
# encoding: utf-8

import socket
import os
client = socket.socket()
ip_port = ('127.0.0.1',9999)
client.connect(ip_port)
path = 'E:/github/py-test/foundation/day5/uploaddemo/BroadcomWLAN[h4wg02ww].exe'
file_name = os.path.basename(path)
file_size = os.stat(path).st_size
#print path,file_name,file_size
file_size = int(file_size)
client.send(str(file_size)+"|"+file_name)

with open(path,'rb') as f:
  flag = client.recv(1024)
  while flag:
    flag = False if file_size<1024 else True
    data = f.read(1024)
    file_size -= 1024
    client.send(data)
client.close()


#第一个发文件名，第二个发送文件大小
#第三个发数据