# 框架介绍
本框架使用Selenium、Appium、Lettuce工具，采用PO设计模式、关键字驱动、数据驱动、BDD，编写中文测试用例，实现Web、Android的UI自动化测试。

由于考虑不同项目的情况，为保持灵活性，本框架对于代码编写部分并未进行过多的封装，使用本框架仍需要一些Python编码基础

测试用例样例：
```
# language: zh-CN

特性: UI自动化测试模版

  场景: 亚马逊商城搜索商品,并检验深圳南山区有货
    Given 我打开谷歌浏览器
    And 我访问亚马逊首页
    When 我在首页，搜索商品"牙刷"
    And 我在商品搜索列表页，点击商品"飞利浦 Sonicare Easy Clean 电动牙刷带声波技术 hx6512"
    And 我切换到浏览器第2个页签
    And 我在商品详情页，点击配送区域选择框
    And 我在商品详情页，点击配送区域-省份框
    And 我点击文字"广东"
    And 我在商品详情页，点击配送区域-城市框
    And 我点击文字"深圳市"
    And 我在商品详情页，点击配送区域-区域框
    And 我点击文字"南山区"
    Then 我在商品详情页，获取现货情况文本
    And 我比较文本与"现在有货"是否相等
    And 我关闭浏览器或设备
```


## 用例分层概念
![](https://github.com/fengyibo963/DemoUITestLettuce/blob/master/docs/%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84(%E5%88%86%E5%B1%82%E6%A6%82%E5%BF%B5).png)

该框架分层使用PO设计模式，同时做了一些改进

* Page（页面）：封装页面为类，并且封装所有操作登录动作(行为)。
* Suite（套件）：封装动作(行为)（例如下拉框选择需要三步"点击下拉框、选择选项、点击确认"，为了更好的复用可以将三步合为一个行为直接调用）。
* TestCase（用例）：使用动作(行为)拼接工作流，并且对于所有动作可以进行断言。

由于某些操作自身就可以定义为动作，因为TestCase既可以使用Suite拼接，也可以使用Page进行拼接（或混合拼接）。

如果为了更好的理解分层，同时增强TestCase脚本的可读性，可以封装所有动作仅使用Suite拼接TestCase（但同时代码量、维护成本会相应的增高，不推荐）。

## 关键字驱动与BDD
本框架使用Lettuce工具实现关键字驱动和BDD，Lettuce实现函数关联关键字并且通过BDD(Given、When、Then)格式编写测试用例。

每个函数绑定一个关键字，通过调用关键字的方式调用函数实现测试用例执行。根据Lettuce的支持可以写中文。

## 数据驱动
对于所有输入参数均进行高度参数化，将需要的所有参数进行参数化，这样使得操作代码的复用性、维护性提高。

所有对于不同的测试场景，仅直接通过不同的测试数据组合实现。

## 数据处理
* 数据库操作
由于一些原因可能需要断言的数据并不能从页面中获取仅仅记录在数据库，或者需要清理自动化

* 数据生成器介绍
业务需要的参数有一些并不能固定设置，例如注册手机号等不可重复参数。

为了做到真正的自动化扩展使用数据生成器，使用生成器按照规则生成想要的数据字典，在编写TestCase的使用直接调用生成器并提取参数即可

## 编写规范介绍
为了代码的可读性，指定了一些编写[规范提供参考（可根据自己喜好修改）](https://github.com/fengyibo963/DemoUITestLettuce/blob/master/docs/%E7%BC%96%E5%86%99%E8%AF%B4%E6%98%8E.md)

## 项目结构详细介绍

![](https://github.com/fengyibo963/DemoUITestLettuce/blob/master/docs/%E9%A1%B9%E7%9B%AE%E7%9B%AE%E5%BD%95.png)

```
|-- config
|    -- env.yaml  # 环境变量
|    -- envSpecify.py  # env环境切换方法
|-- features
|    -- common      
|        -- common.py  # selenium、appium基础通用方法，使用过程中可以根据需要自行拓展
|        -- getDriver.py  # 启动浏览器、APP获取driver
|        -- readConfig.py  # 读取相关配置等内容进入全局变量
|    -- data
|        -- dataCreate  # 测试数据生成
|            -- xxxx.py  # 某些特殊数据的生成
|        -- dbOperation  # 数据库数据操作  
|            -- xxxx.py  # 某些数据库操作的封装
|    -- pages
|        -- xxxx.py  # 该产品某一页面
|    -- suites
|        --xxxx.py  # 该产品通用封装的模块
|    -- testcases
|        -- xxx.feature  # 测试用例文件
|-- runcase.py     # 通过参数执行任一测试用例或测试用例集合
|-- requirements.txt    # 该文件记录所有需要用的框架（以便更换环境一键安装）
```

# 环境/使用介绍
## 环境安装说明
* 安装Python3环境
* 安装相关模块库
```
pip3 install -r requirements.txt
```
## Lettuce
* 替换Lettuce版本

由于官方lettuce只支持python2，需替换lettuce版本
```
pip3 uninstall lettuce # 卸载lettuce
git clone https://github.com/sgpy/lettuce.git  # clone大佬源码在任意位置
cd lettuce  # 进入源码项目
git checkout -b py3 origin/py3  # 创建python3分支并clone
sudo python3 setup.py install  # 安装支持python3的版本
lettuce --version  # 检查版本号看是否安装成功
```
## Selenium
* 下载浏览器驱动

对于Web的UI自动化测试需要使用浏览器驱动，根据不同的浏览器下载相应的驱动即可

例如Chrome浏览器需要下载ChromeDriver驱动(注意下载对应版本的驱动)，并放置指定位置
```
驱动下载地址1：http://npm.taobao.org/mirrors/chromedriver/
驱动下载地址2：http://chromedriver.storage.googleapis.com/index.html

ubuntu
sudo mv chromedriver /usr/bin/chromedriver

mac
sudo mv chromedriver /usr/local/bin

windows放在python安装路径的Scripts/文件下
C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts
```
## Appium
客户端下载地址：https://github.com/appium/appium-desktop/releases

Ubuntu安装参考[指南](https://blog.csdn.net/baidu_36943075/article/details/103985826)

Mac安装参考指南[指南](https://www.jianshu.com/p/d36ff3707862)

Windows安装参考[指南](https://www.cnblogs.com/lgqboke/p/9776503.html)

## 配置说明
配置env环境参数
* config/env.yaml文件,用于数据库连接、host设置
* 可以添加更多环境，直接添加相应的envXx.yaml文件即可，运行用例时使用Xx作为环境参数即可 
* 当需要多环境执行时，env.yaml文件变为数据传输中介不再需要维护

## 用例执行说明
runcase.py脚本为功能测试用例执行统一入口

**查看帮助--help**
```
python3 runcase.py --help
usage: runcase.py [-h] [--env ENV] [--collection COLLECTION] --name NAME

optional arguments:
  -h, --help            show this help message and exit
  --env ENV, -e ENV     环境变量参数，非必要参数
  --collection COLLECTION, -c COLLECTION
                        测试用例集合名称，非必要参数(testcases中用于划分用例集合的文件夹名,当未划分用例集合时不需要)
  --name NAME, -n NAME  测试用例名称，必要参数，例：case1 或者 case1,case2
```

**执行用例**

```
python3 runcase.py -n $env -c $collection -n $name  # 在$env环境下,testcases/$collection文件夹路径,$name文件名称或all(all即可该文件下所有用例)
例：
python3 runcase.py -n goodsInStock
python3 runcase.py -n all
python3 runcase.py -c smoke -n all
```
