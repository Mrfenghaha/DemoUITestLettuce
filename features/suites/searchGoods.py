# -*- coding:utf-8 -
from lettuce import *


@step('我在Top，搜索商品"(.*?)"')
def search_good(step, text):
    step.behave_as("""
            Given 我在Top，操作输入框并输入"{text}"
            When 我在Top，点击搜索按钮
        """.format(text=text))

