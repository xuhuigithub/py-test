#!/bin/env python
#coding:utf-8
import socket

client = socket.socket()
ip_port = ('127.0.0.1',9999)
client.connect(ip_port)
client.send('hello')
while True:
  data = client.recv(1024)
  print data
  inp = raw_input('client:')
  client.send(inp)
  if inp == 'exit':
    break
client.close()