#!/bin/env python
#coding:utf-8
import SocketServer
from SocketServer import TCPServer
TCPServer.request_queue_size = 65535

class Myserver(SocketServer.BaseRequestHandler):
  #继承SocketServer没有构造函数，去执行BaseRequestHandler的构造函数
  #
  def setup(self):
    #当连接建立时处理的动作
    print 'haha'
    self.request.send('hello')
  
  def handle(self):
    print self.request
    conn =  self.request
    flag = True
    while flag:
      data = conn.recv(1024)
      #recv 也是阻塞的
      flag = False if data == 'exit' else True
      print data
      server_data = raw_input('server:')
      conn.send(server_data)
    
  def finish(self):
    #当连接结束时处理的动作
    print 'hehe'


if __name__ == "__main__":
    ip_port = ('127.0.0.1',9999)
    server = SocketServer.ThreadingTCPServer(ip_port,Myserver)
    #ThreadingTCPServer继承(ThreadingMixIn, TCPServer)
    #ThreadingMixIn没有构造函数 执行TCPServer的
    #TCPServer 继承BaseServer 执行了BaseServer的构造函数
    #真正的多线程处理请求的核心在BaseServer.serve_forever这里
    server.serve_forever()
    #poll_interval
    
