# -*- coding: utf-8 -*-
import os
import yaml
from lettuce import *
cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


@step(u'获取系统环境变量参数')
def file_creation(step):
    # 获取文件位置
    file_path = FileCreation().file_creation()
    # 读取环境变量
    config = ReadConfig().read_config(file_path)
    world.config = config


# 创建默认配置文件
class FileCreation:
    def __init__(self):
        self.config_path = os.path.join(cur_path, 'config')
        self.env_yaml_path = os.path.join(self.config_path, 'env.yaml')
        self.android_path = os.path.join(self.config_path, 'android.yaml')

    def create_config_file(self):
        # 如果没有config文件夹，就创建一个
        if not os.path.exists(self.config_path):
            os.mkdir(self.config_path)  # 创建config文件夹

        # 如果没有config/env.yaml,自动创建并写入默认值
        if not os.path.exists(self.env_yaml_path):
            with open(self.env_yaml_path, 'w') as file:
                file.write('# host环境IP\nhost: https://www.amazon.cn\n'
                           '# mysql服务信息\nmysql_info:\n  ip: xxxx\n  port: 3306\n  account: xxxx\n  password: xxxx\n'
                           '# mongodb服务信息\nmongodb_info:\n  ip: xxxx\n  port: 3306\n  account: xxxx\n  password: xxxx\n')
            file.close()

        # 如果没有config/android.yaml,自动创建并写入默认值
        if not os.path.exists(self.android_path):
            with open(self.android_path, 'w') as file:
                file.write('app_info:\n'
                           '  # APP名称\n  appName: xxx\n'
                           '  # APP包名\n  appPackage: xxx\n'
                           '  # APP程序名\n  appActivity: xxx\n'
                           'device_info:\n'
                           '  # 设备版本号\n  platformVersion: 6.0\n'
                           '  # 设备id\n  deviceName: 192.168.58.104:5555\n'
                           'appium_info:\n'
                           '  #appium所在ip以及端口号\n  appiumIp: http://127.0.0.1:4723/wd/hub\n')
            file.close()

    def file_creation(self):
        self.create_config_file()
        file_path = {
            "config_path": self.config_path,
            "env_yaml_path": self.env_yaml_path,
            "android_yaml_path": self.android_path,
        }
        return file_path


# 读取配置文件
class ReadConfig:

    def read_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            # 使用load方法将读出的字符串转字典
            content = yaml.full_load(file)
            file.close()
        return content

    def read_config(self, path):
        android_content = self.read_yaml_file(path["android_yaml_path"])
        env_content = self.read_yaml_file(path["env_yaml_path"])

        config = {
            # APP信息
            "app_info": android_content['app_info'],
            # 设备信息
            "device_info": android_content['device_info'],
            # appium信息
            "appium_info": android_content['appium_info'],
            # host地址
            "host": env_content['host'],
            # mysql数据库信息
            "mysql_info": env_content['mysql_info'],
            # mongodb信息
            "mongodb_info": env_content['mongodb_info']
        }

        return config
