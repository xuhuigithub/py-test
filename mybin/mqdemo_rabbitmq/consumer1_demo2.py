#!/bin/env python
#coding:utf-8

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()

def callback(ch,method,properties,body):
  print " [x] Received %r" % body
  time.sleep(body.count(b'.'))  #消息中有几个.睡几秒
  print "[x] Done"
channel.basic_consume(consumer_callback=callback,
                      queue='hello',
                      no_ack=True #默认开启ack,指定这个参数关闭，ack指的是当worker处理完收到的消息后会向RabbitMQ回复一个消息告诉他可以把消息删除了
                      )
channel.basic_qos(prefetch_count=1)

print' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()