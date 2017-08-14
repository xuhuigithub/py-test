# !/usr/bin/env python
# encoding: utf-8

import socket
import os
client = socket.socket()
ip_port = ('127.0.0.1',9999)
client.connect(ip_port)
#path = 'E:/github/py-test/foundation/day5/uploaddemo/test.log'


#print path,file_name,file_size


while True:
  cmd = raw_input('cmd')  #cmd = self.request.recv(3)
  client.send(cmd)
  if cmd == 'put':
    remote_path = raw_input('remote_path')
    client.send(remote_path) #recv_path = self.request.recv(256)
    put_file = raw_input('pls input local file path')
    file_name = os.path.basename(put_file)
    file_size = os.stat(put_file).st_size
    allow = bool(int(client.recv(1024))) #self.request.send('1')
    if allow:
      with open(put_file,'rb') as f:
        client.send(str(file_size) + "|" + file_name)
        print str(file_size) + "|" + file_name
        flag = client.recv(1024)
        file_size = int(file_size)
        while flag:
          flag = False if file_size<1024 else True
          data = f.read(1024)
          file_size -= 1024
          client.send(data)
        continue
  elif cmd == 'get':
    remote_path = raw_input('pls input remote path')
    local_filename = os.path.basename(remote_path)
    client.send(remote_path)
    client.recv(1024)
    recv_path = raw_input('pls input local path')
    recv_filename = os.path.join(recv_path,local_filename)
    flag = client.recv(1024)
    with open(recv_filename,'wb') as f:
      client.send('True')
      file_size = client.recv(1024)
      file_size = int(file_size)
      while flag:
        flag = False if file_size < 1024 else True
        data = client.recv(1024)
        f.write(data)
        file_size -= 1024
      continue
  else:
    client.close()
    break


#第一个发文件名，第二个发送文件大小
#第三个发数据