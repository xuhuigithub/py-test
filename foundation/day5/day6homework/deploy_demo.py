#!/bin/env python
#coding:utf-8
import threading
import paramiko
import Queue
import yaml
with open('inventory_demo.yml','r') as f:
  data = yaml.load(f)
host_queue = Queue.Queue()
class deploy(object):
  def __init__(self,remotehost,remoteuser,remotepassword,remotekey=None,remoteport=22):
    self.ssh = paramiko.SSHClient()
    self.remotehost = remotehost
    self.remoteuser = remoteuser
    self.remotepassword = remotepassword
    self.remotekey = remotekey
    self.remoteport = remoteport
  def varify(self):
    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    self.ssh.connect(self.remotehost, self.remoteport, self.remoteuser,self.remotepassword)
  def remote_command(self,exec_command):
    self.varify()
    try:
      stdin,stdout,stderr = self.ssh.exec_command(exec_command)
    except Exception:
      print '执行命令出错'
    else:
      print stdout.read()
for host in data['host_info']:
  host_queue.put(deploy(host['ip'],host['username'],host['password']))
# stdin,stdout,stderr = host_41.remote_command('ls')
# print stdout.read()
# t1 = threading.Thread(target=host_41.remote_command,args=('ls',))
# print t1.start()
while True:
  if host_queue.qsize() > 0:
    threading.Thread(target=host_queue.get().remote_command,args=('yum install httpd -y',)).start()
  else:
    break