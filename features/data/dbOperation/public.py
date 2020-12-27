# -*- coding: utf-8 -*-
import pymysql
import pymongo
import urllib
from lettuce import *


@step(u'连接Mysql数据库，并执行"(.*?)"语句')
def execute_mysql(step, sql):
    mysql_info = world.config['mysql_info']
    db = pymysql.connect(host=mysql_info['ip'], port=mysql_info['port'], user=mysql_info['mysql_account'],
                         password=mysql_info['password'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return cursor


@step('连接MonGoDB数据库')
def client_mongodb(step, database):
    mongodb_info = world.config['mongodb_info']
    account = urllib.quote_plus(mongodb_info['account'])
    password = urllib.quote_plus(mongodb_info['password'])
    mongodb = "mongodb://%s:%s@%s:%s/%s" % (account, password, mongodb_info['ip'], mongodb_info['port'], database)
    client = pymongo.MongoClient(mongodb)
    return client
