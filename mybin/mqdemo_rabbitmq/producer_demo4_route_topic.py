#!/bin/env python
#coding:utf-8

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()

channel.exchange_declare(exchange='topic_level',
                         exchange_type='topic')


routing_key = sys.argv[1] if len(sys.argv) > 2 else 'emergency.po' #level.group

message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)

print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()