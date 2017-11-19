#!/bin/env python
#coding:utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()
channel.queue_declare(queue='hello')
#创建一个队列， If we send a message to non-existing location, RabbitMQ will just drop the message.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print "[x] Sent 'Hello World!'"

connection.close()