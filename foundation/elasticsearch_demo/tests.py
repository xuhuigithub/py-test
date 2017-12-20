#!/usr/bin/env python
# encoding: utf-8
from elasticsearch import Elasticsearch
import time, MySQLdb


def time_count(func):
    def inner(*args):
        s_time = int(round(time.time() * 1000))
        data = func(*args)
        elapsed_time = int(round(time.time() * 1000)) - s_time
        print elapsed_time
        return data

    return inner


def init_db(**kwargs):
    db = MySQLdb.connect(**kwargs)
    return db


@time_count
def main():
    db_dict = {'host': "192.168.206.132", 'port': 3307, 'user': "root", 'passwd': "123456", 'db': "dpm_es_count",
               'charset': "UTF8"}
    query_param = {
        "range": {
            "logTimestamp": {
                "lt": "now",
            }
        }
    }
    db = init_db(**db_dict)
    cursor = db.cursor()
    sql = "INSERT INTO order_monitor_es(customername,entname,executetime) values(%s,%s,%s)"
    es = Elasticsearch(['192.168.206.80:9200', '192.168.206.81:9200', '192.168.206.82:9200'])
    res = es.search(index='enterprise_log_2017_12', body={"query": query_param}, size=10000,
                    _source_include=['customerFullName', 'entname', 'executeTime'])
    ent_logs = res['hits']['hits']
    data = [(log['_source']['customerFullName'], log['_source'].get('entname'), log['_source']['executeTime'],) for log
            in ent_logs]
    try:
        cursor.executemany(sql, tuple(data))
        db.commit()
    except:
        db.rollback()
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    main()
