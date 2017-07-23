from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
conn = MongoClient('192.168.61.137',connectTimeoutMS=2)
try:
  conn.admin.command('ismaster')
except ConnectionFailure:
  print "hehe"
else:
  print ok
finally:
  conn.close()