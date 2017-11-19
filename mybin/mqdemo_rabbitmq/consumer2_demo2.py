#!/bin/env python
#coding:utf-8

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()

def callback(ch,method,properties,body):
  print " [x] Received %r" % body
  print ch,method,properties
  time.sleep(body.count(b'.'))  #消息中有几个.睡几秒
  print "[x] Done"
channel.basic_consume(consumer_callback=callback,
                      queue='hello',
                      no_ack=True)

channel.basic_qos(prefetch_count=1) #每次最多处理多少消息
print' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()