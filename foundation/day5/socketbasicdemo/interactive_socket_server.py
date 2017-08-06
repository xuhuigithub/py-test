#!/bin/env python
#coding:utf-8
import socket
sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)

sk.listen(5)
while True:
  conn,address = sk.accept()
  conn.send('hello')
  flag = True
  while flag:
    data = conn.recv(1024)
    #recv 也是阻塞的
    flag = False if data == 'exit' else True
    print data
    conn.send('sb')
  conn.close()