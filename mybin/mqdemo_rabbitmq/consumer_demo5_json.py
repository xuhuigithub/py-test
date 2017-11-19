#!/bin/env python
#coding:utf-8

import pika
import json
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()

def callback(ch,method,properties,body):
  data = json.loads(body)
  print data,type(data)
  print " [x] Received %r" % body
  print "[x] Done"

channel.basic_consume(consumer_callback=callback,
                      queue='hello',
                      no_ack=True
                      )
channel.basic_qos(prefetch_count=1)

print' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()