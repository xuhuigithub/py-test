#!/bin/env python
#coding:utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()

def callback(ch,method,properties,body):
  print " [x] Received %r" % body

channel.basic_consume(consumer_callback=callback,
                      queue='hello',
                      no_ack=True)

print' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()