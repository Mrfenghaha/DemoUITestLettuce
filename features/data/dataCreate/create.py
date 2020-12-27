# -*- coding: utf-8 -*-
import time
from lettuce import *


@step(u'创建自定义测试数据')
def create(step):
    test_data = {}
    test_data[u'时间戳'] = str(round(time.time() * 1000))[4:13]  # 由时间戳号生成的手机
    test_data[u'密码'] = "password"  # 由时间戳号生成的手机
    world.test_data = test_data
