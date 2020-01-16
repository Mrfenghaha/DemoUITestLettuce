# -*- coding: utf-8 -
from lettuce import *
from selenium.webdriver.common.by import By
"""
亚马逊-添加商品入购物车成功页
"""


@step('我在加入购物车成功页面，获取加入结果文本')
def get_add_success(step):
    element = world.element['addToCartSuccess_addResult'] = (By.ID, 'huc-v2-order-row-confirm-text')
    world.text = world.driver.find_element(*element).text


@step('我在加入购物车成功页面，获取购物车金额文本')
def get_amount(step):
    element = world.element['addToCartSuccess_shopCartAmount'] = (By.XPATH, '//*[@id="hlb-subcart"]/div[1]/span/span[2]')
    world.text = world.driver.find_element(*element).text
