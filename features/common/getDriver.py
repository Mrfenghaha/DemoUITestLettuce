# -*- coding: utf-8 -*-
import os
from lettuce import *
from selenium import webdriver as selenium_driver
from appium import webdriver as appium_driver
cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


@step(u'打开(.*)浏览器')
def get_driver_for_browser(step, browser):
    # 加载通用
    step.behave_as(u'And 获取系统环境变量参数\n'
                   u'And 获取被测系统元素列表\n'
                   u'And 创建自定义测试数据')
    if browser == "谷歌":
        # 谷歌浏览器规避监测
        option = selenium_driver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 启动谷歌浏览器
        world.driver = selenium_driver.Chrome(options=option)  # 获取driver，并设置规避监测
    elif browser == "谷歌无头":
        # 谷歌浏览器规避监测
        option = selenium_driver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 设置谷歌无头浏览器
        chrome_options = selenium_driver.ChromeOptions()
        chrome_options.add_argument('--headless')
        # 启动谷歌浏览器
        world.driver = selenium_driver.Chrome(chrome_options=chrome_options, options=option)  # 使用无头浏览器，获取driver，并设置规避监测
    elif browser == "火狐":
        # 设置谷火狐无头浏览器
        options = selenium_driver.FirefoxOptions()
        options.add_argument('--headless')
        # 启动火狐浏览器
        world.driver = selenium_driver.Firefox()  # 获取driver
    elif browser == "火狐无头":
        # 设置谷火狐无头浏览器
        options = selenium_driver.FirefoxOptions()
        options.add_argument('--headless')
        # 启动火狐浏览器
        world.driver = selenium_driver.Firefox(options=options)  # 使用无头浏览器，获取driver
    elif browser == "Safari":
        # 启动safari浏览器
        world.driver = selenium_driver.Safari()
    else:
        # 谷歌浏览器规避监测
        option = selenium_driver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 启动谷歌浏览器
        world.driver = selenium_driver.Chrome('%s' % driver_path, options=option)  # 获取driver，并设置规避监测
    world.driver.maximize_window()  # 将浏览器窗口最大化
    world.driver.implicitly_wait(10)  # 设置隐形等待直至加载完成


@step(u'关闭浏览器')
def close(step):
    world.driver.quit()


@step(u'打开APP并设置重启为"(.*?)"')  # true或false
def get_driver_for_chrome(step, reset):
    # 加载通用
    step.behave_as(u'Given 获取系统环境变量参数\n'
                   u'And 获取被测系统元素列表\n'
                   u'And 创建自定义测试数据')

    app_apk_path = os.path.join(cur_path, 'app', '%s.apk' % world.config["app_info"]['appName'])
    start_info = {
        # 平台名称
        "platformName": 'Android',
        # 平台版本号
        "platformVersion": str(world.config["device_info"]['platformVersion']),
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

    world.appium_driver = appium_driver.Remote(world.config["appium_info"]['appiumIp'], start_info)


@step(u'关闭移动设备')
def close(step):
    world.appium_driver.quit()


@step(u'访问系统首页')
def visit_website(step):
    world.driver.get(world.config['host'])
    # step.behave_as(u'Given 我查询"浏览器私密链接_高级按钮"是否存在')
    # if world.exist is True:
    #     step.behave_as(u'Given 我点击"浏览器私密链接_高级按钮"\n'
    #                    u'And 我点击"浏览器私密链接_继续访问按钮')
    # else:
    #     pass
