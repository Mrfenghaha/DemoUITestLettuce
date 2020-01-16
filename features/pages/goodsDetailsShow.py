# -*- coding: utf-8 -
from lettuce import *
from selenium.webdriver.common.by import By
"""
商品详情展示页
"""


@step('我在商品详情页，点击加入购物车按钮')
def click_add_action(step):
    element = world.element['goodsDetails_addToCartButton'] = (By.ID, 'add-to-cart-button')
    world.driver.find_element(*element).click()


@step('我在商品详情页，点击配送区域选择框')
def click_add_action(step):
    element = world.element['goodsDetails_deliveryAreaSelect'] = (By.ID, 'ddmSelectedAddressText')
    world.driver.find_element(*element).click()


@step('我在商品详情页，点击配送区域（省）选择框')
def click_add_action(step):
    element = world.element['goodsDetails_deliveryAreaSelectState'] = (By.ID, 'ddmStateTriggerId')
    world.driver.find_element(*element).click()


@step('我在商品详情页，点击配送区域（市）选择框')
def click_add_action(step):
    element = world.element['goodsDetails_deliveryAreaSelectCity'] = (By.ID, 'ddmCityTriggerId')
    world.driver.find_element(*element).click()


@step('我在商品详情页，点击配送区域（区）选择框')
def click_add_action(step):
    element = world.element['goodsDetails_deliveryAreaSelectDistrict'] = (By.ID, 'ddmDistrictTriggerId')
    world.driver.find_element(*element).click()


@step('我在商品详情页，获取现货情况文本')
def get_amount(step):
    element = world.element['goodsDetails_inventorySituation'] = (By.XPATH, '//*[@id="ddmAvailabilityMessage"]/span')
    world.text = world.driver.find_element(*element).text
