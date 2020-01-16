# -*- coding:utf-8 -
import os
from lettuce import *
from selenium import webdriver as selenium_driver
from appium import webdriver as appium_driver
cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


@step('我打开谷歌浏览器')
def get_driver_for_chrome(step):
    # 加载通用
    step.behave_as("""
            Given 我获取系统环境变量参数
            And 我获取被测系统元素列表
        """)

    world.driver = selenium_driver.Chrome()  # 获取driver
    world.driver.maximize_window()  # 将浏览器窗口最大化
    world.driver.implicitly_wait(10)  # 设置隐形等待直至加载完成


@step('我打开APP并设置重启为"(.*?)"')  # true或false
def get_driver_for_chrome(step, reset):
    # 加载通用
    step.behave_as("""
            Given 我获取系统环境变量参数
            And 我获取被测系统元素列表
        """)

    app_apk_path = os.path.join(cur_path, 'app', world.config["app_info"]['appName'])
    start_info = {
        # 平台名称
        "platformName": 'Android',
        # 平台版本号
        "platformVersion": world.config["device_info"]['platformVersion'],
        # 设备名称
        'deviceName': world.config["device_info"]['deviceName'],
        # app文件地址
        'app': app_apk_path,
        # app包名
        'appPackage': world.config["app_info"]['appPackage'],
        # app程序名
        'appActivity': world.config["app_info"]['appActivity'],
        # 是否不每次重新安装
        'noReset': reset != "true",
        # 是否启用unicode键盘，启动可以输入中文
        'unicodeKeyboard': True,
        # 是否每次重新安装键盘
        'resetKeyboard': True,
        # 如果达到超时时间仍未接收到新的命令时appium会自动结束会话/秒
        'newCommandTimeout': 600}

    driver = appium_driver.Remote(world.config["appium_info"]['appiumIp'], start_info)
    return driver


@step('我关闭浏览器或设备')
def close(step):
    world.driver.quit()


# 将被测系统元素写入一个元素列表,用于随时提取使用(有一些操作需要元素才能完成)，因此被测系统的元素名称要保持独立性
@step('我获取被测系统元素列表')
def element_list(step):
    world.element = {}
