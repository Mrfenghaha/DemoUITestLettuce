# language: zh-CN

特性: UI自动化测试模版

  场景: 亚马逊商城搜索商品并加入购物车，检验是否添加成功以及金额
    Given 我打开谷歌浏览器
    And 我访问亚马逊首页
    When 我在Top，搜索商品"牙刷"
    And 我在商品搜索列表页，点击商品"惠百施 熊本熊 成人牙刷 （颜色随机）"（自动翻页）
    And 我切换到浏览器第2个页签
    And 我在商品详情页，点击加入购物车按钮
    Then 我在加入购物车成功页面，获取加入结果文本
    And 我比较文本与"商品已加入购物车"是否相等
    And 我在加入购物车成功页面，获取购物车金额文本
    And 我比较文本与"￥ 81.54"是否相等
    And 我关闭浏览器或设备
