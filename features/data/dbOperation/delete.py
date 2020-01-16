# -*- coding: utf-8 -
from lettuce import *


@step('我在数据库，通过ID"(.*?)"删除系统')
def delete_system(step, id):
    sql = "delete from xxx.xxx where id = '%s'" % id
    step.behave_as("""Given 我连接Mysql数据库，并执行"{sql}"语句""".format(sql=sql))
