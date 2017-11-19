#!/bin/env python
#coding:utf-8

import pika
import json

params = {
  'name': 'xuhui',
  'age': 12
}

json_params = json.dumps({'data':params})

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      properties=pika.BasicProperties(
                        content_type='application/json' #貌似是加不加不影响，但还是加上吧
                      ),
                      body=json_params)
print "[x] Sent json"

connection.close()