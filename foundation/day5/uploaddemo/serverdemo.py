# !/usr/bin/env python
# encoding: utf-8
import os
import SocketServer

uploadpath = "C:/temp"
class Myserver(SocketServer.BaseRequestHandler):
  def setup(self):
    print self.client_address,"connect"

  def cmd_upload(self,recv_path):
    conn = self.request
    flag = True
    datasize,filename = conn.recv(1024).split('|')
    print datasize
    datasize = int(datasize)
    filepath = os.path.join(recv_path, filename)
    #C:/temp
    with open(filepath, 'wb') as f:
      conn.send(str(flag))
      while flag:
        recv_data = conn.recv(1024)
        flag = False if datasize <= 1024 else True
        f.write(recv_data)
        datasize -= 1024
        print  datasize
  def cmd_get(self,get_path):
    conn = self.request
#    get_path = conn.recv(1024)
    try:
      file_size = os.stat(get_path).st_size
      file_size = int(file_size)
    except Exception:
      print "error"
      conn.send('False')
    else:
      conn.send('True')
    flag = conn.recv(1024)
    conn.send(str(file_size))
    with open(get_path, 'rb') as f:
      while flag:
        flag = False if file_size < 1024 else True
        data = f.read(1024)
        conn.send(data)
        file_size -= 1024

  def handle(self):
    while True:
      cmd = self.request.recv(3)
      recv_path = self.request.recv(256)
      self.request.send('1')
      if cmd == 'put':
        self.cmd_upload(recv_path)
        continue
      elif cmd == 'get':
        self.cmd_get(recv_path)
        continue

  def finish(self):
    print self.client_address,"break"

if __name__ == '__main__':
  ip_port = ('127.0.0.1',9999)
  server = SocketServer.ThreadingTCPServer(ip_port,Myserver)
  server.serve_forever()
