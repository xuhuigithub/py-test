#!/bin/env python
#coding:utf-8
import socket
sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)

sk.listen(5)
while True:
  conn,address = sk.accept()
  conn.send('hello,%s' %(address[0]))
  flag = True
  while flag:
    data = conn.recv(1024)
    #recv 也是阻塞的
    flag = False if data == 'exit' else True
    print data
    server_data = raw_input('server:')
    conn.send(server_data)
  conn.close()