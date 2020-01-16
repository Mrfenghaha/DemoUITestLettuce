# -*- coding:utf-8 -
from lettuce import *
from selenium.webdriver.common.by import By
"""
    页面顶部部分（所有页面均有）
"""


@step('我在Top，操作输入框并输入"(.*?)"')
def send_search_action(step, text):
    element = world.element['top_searchInput'] = (By.ID, 'twotabsearchtextbox')
    world.driver.find_element(*element).send_keys(text)


@step('我在Top，点击搜索按钮')
def click_submit_action(step):
    element = world.element['top_searchButton'] = (By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input')
    world.driver.find_element(*element).click()