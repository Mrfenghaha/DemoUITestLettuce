# -*- coding:utf-8 -
from lettuce import *
from selenium.webdriver.common.by import By
"""
首页
"""


@step('我访问亚马逊首页')
def visit_website(step):
    world.driver.get(world.config["host"])
