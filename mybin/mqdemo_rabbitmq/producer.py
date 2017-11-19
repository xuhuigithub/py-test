#!/bin/env python
#coding:utf-8

import pika
import json

params = {
  'name': 'xuhui',
  'age': 12
}

credentials = pika.PlainCredentials('guest', 'guest')

json_params = json.dumps({'data':params})

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789,credentials=credentials,virtual_host='/'))
channel = connection.channel()

# result = channel.queue_declare(exclusive=True)
# queue_name = result.method.queue
# # 创建一个临时queue一旦消费者取消连接 队列将被删除，当exclusive=True时

channel.queue_declare(queue='New_queue',durable=True) #创建一个新queue并开启初始化

channel.basic_publish(exchange='',
                      routing_key='hello',
                      properties=pika.BasicProperties(
                        delivery_mode=2,# 开启持久化
                        content_type='application/json' #貌似是加不加不影响，但还是加上吧
                      ),
                      body=json_params)

print "[x] Sent json"

connection.close()