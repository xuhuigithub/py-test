#!/bin/env python
#coding:utf-8
import socket

#1、创建socket
client = socket.socket()
#2、连接server端
ip_port = ('127.0.0.1',9999)
client.connect(ip_port)
#3、客户端接收
data = client.recv(8193)
#recv有一个缓冲区 这个参数（1024）的意思是一次最多只能拿1024个字节的文件
#缓冲区的一般大小为8k，设置时不要大于8k
print len(data)