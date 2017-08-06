#!/bin/env python
#coding:utf-8
import socket
#1、创建socket对象
a = [1]
data = a*8193
data = str(data)
sk = socket.socket()
ip_port = ('127.0.0.1',9999)
#2、绑定地址bind
sk.bind(ip_port)
#3、 监听listen,这个5代表最大连接数
sk.listen(5)
while True:
  #4、 接受请求
  conn,address = sk.accept()
  #5、回复请求
  conn.send(data)
  #send 先将消息发送到自己的缓冲区内然后再发送至对端
  #6、 关闭
  conn.close()