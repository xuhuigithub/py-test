#!/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
def SMS(receiver,msg):
  url = 'http://192.168.11.171:8005/sendMessage'
  values = {'to' : receiver,
            'param' : msg,
            'flag' : '1' }
  headers = { 'cache-control':'no-cache','content-type':'application/json','postman-token' : '9f981ea5-35e7-9a18-1be5-1456050d4249'}
  data = json.dumps(values)
  req = urllib2.Request(url, data, headers)
  try:
    response = urllib2.urlopen(req)
  except urllib2.URLError as e:
    print e.reason
  except urllib2.HTTPError as e:
    print e.code,e.reason
  else:
    return response

if __name__ == '__main__':
  response = SMS(receiver=17710399068,msg= "test")
  the_page = response.read()
  code = response.getcode()
  print the_page,code
