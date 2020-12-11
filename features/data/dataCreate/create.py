# -*- coding: utf-8 -
import time
from lettuce import *


@step('我创建自定义测试数据')
def create(step):
    world.test_data = {
        "时间戳": str(round(time.time() * 1000))[4:13],  # 由时间戳号生成的手机
        "密码": "password"
    }
