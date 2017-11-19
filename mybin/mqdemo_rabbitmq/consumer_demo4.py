#!/bin/env python
#coding:utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

queue_name = 'route_topic_demo_emergency for group: po'

channel.queue_declare(queue_name)



channel.queue_bind(exchange='topic_logs',
                   queue=queue_name,
                   routing_key='emergency.*')

#* (star) can substitute for exactly one word.用来替代一个单词
# (hash) can substitute for zero or more words.用来替代所有单词
# 不过滤接收所有消息："#"
# 如果一个消息被两个worker同时匹配成功那么两个worker都会处理消息

print(' [*] Waiting for emergency message. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()