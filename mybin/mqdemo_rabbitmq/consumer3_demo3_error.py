#!/bin/env python
#coding:utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.206.132',port=32789))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

channel.queue_declare('route_demo_error')



channel.queue_bind(exchange='direct_logs',
                   queue='route_demo_error',
                   routing_key='error')

print(' [*] Waiting for error logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue='route_demo_error',
                      no_ack=True)

channel.start_consuming()