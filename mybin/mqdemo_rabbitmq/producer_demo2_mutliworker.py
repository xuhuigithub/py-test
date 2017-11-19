#!/bin/env python
#coding:utf-8
import pika
import sys


message = ' '.join(sys.argv[1:]) or "Hello World...."
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()
channel.queue_declare(queue='hello') #创建一个queue，durable是开启持久化
#创建一个队列， If we send a message to non-existing location, RabbitMQ will just drop the message.
channel.basic_publish(exchange='',
                      routing_key='hello',    #queue名称
                      body=message,
                      properties=pika.BasicProperties(
                        delivery_mode=2,
                      ))

print "[x] Sent %r" %message

connection.close()