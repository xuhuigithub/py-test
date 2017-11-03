#!/bin/env python
#coding:utf-8
from smtplib import SMTP
import socket
from sys import platform

class Mysmtplib(SMTP):
  def __init__(self,timeout):
    # super(Mysmtplib,self).__init__(timeout=timeout)
    SMTP.__init__(self,timeout=timeout)

  def connect(self, host='localhost', port=0,keepalvie=False,**keepalive_kwargs):
    SMTP.connect(self,host=host,port=port)
    if keepalvie:
      after_idle_sec = keepalive_kwargs.get('after_idle_sec')
      interval_sec = keepalive_kwargs.get('interval_sec')
      max_fails = keepalive_kwargs.get('interval_sec')
      if platform == "linux" or platform == "linux2":
        #Linux
        """Set TCP keepalive on an open socket.
        It activates after 1 second (after_idle_sec) of idleness,
        then sends a keepalive ping once every 3 seconds (interval_sec),
        and closes the connection after 5 failed ping (max_fails), or 15 seconds
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 3)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)
        """
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, int(after_idle_sec))
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, int(interval_sec))
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, int(max_fails))
      elif platform == "darwin":
        #OS X
        TCP_KEEPALIVE = 0x10
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.sock.setsockopt(socket.IPPROTO_TCP, TCP_KEEPALIVE, int(interval_sec))
      elif platform == "win32":
        #Windows
        pass


if __name__ == "__main__":
  keepalive_kwargs = {'after_idle_sec':1,'interval_sec':3,'max_fails':5}
  smtpObj=Mysmtplib(timeout=20)
  smtpObj.connect('smtp.chinadaas.com',25,keepalvie=True,**keepalive_kwargs)
  smtpObj.login('xuhui@chinadaas.com','****')
  smtpObj.close()

