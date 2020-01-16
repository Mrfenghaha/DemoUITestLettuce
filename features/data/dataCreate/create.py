# -*- coding: utf-8 -
import time
from lettuce import *


@step('我创建自定义测试数据')
def create(step):
    world.custom_test_data = {
        "phone": str(round(time.time() * 1000))[4:13],  # 由时间戳号生成的手机
        "password": "password"
    }
