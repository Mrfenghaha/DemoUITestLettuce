# -*- coding: utf-8 -
from lettuce import *
from selenium.webdriver.common.by import By
"""
商品搜索列表页
"""


@step('我在商品搜索列表页，点击商品"(.*?)"（不自动翻页）')
def click_name_action(step, name):
    element = world.element['searchList_goodsButton'] = (By.XPATH, '//*[text()="' + name + '"]')
    world.driver.find_element(*element).click()


@step('我在商品搜索列表页，点击商品"(.*?)"（自动翻页）')
def click_name_action(step, name):
    world.element['searchList_nextPageButton'] = (By.XPATH, '//*[text()="下一页"]')
    # 点击商品，如果商品不存在就再次点击下一页按钮，最多10次
    step.behave_as("""
                Given I click text "{a}", if the text not exist, will try again click element "{el}", maximum 10 times
            """.format(a=name, el='searchList_nextPageButton'))


@step('我在商品搜索列表页，点击下一页按钮')
def click_last_action(step):
    element = world.element['searchList_nextPageButton'] = (By.XPATH, '//*[text()="下一页"]')
    world.driver.find_element(*element).click()
