# -*- coding:utf-8 -
import time
from lettuce import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


# ````````````````````````````````````````基础操作封装````````````````````````````````````````
@step('我点击"(.*?)"')
def click_element(step, element):
    element = world.element[element]
    world.driver.find_element(*element).click()


@step('我点击一下"(.*?)"，如果不存在，我将点击"(.*?)"后再次尝试点击，最多(.*)次')
def click_element_retry(step, element_a, element_b, num):
    element_a = world.element[element_a]
    element_b = world.element[element_b]
    for n in range(int(num)):
        try:
            world.driver.find_element(*element_a)
        except NoSuchElementException:
            world.driver.find_element(*element_b).click()
        else:
            world.driver.find_element(*element_a).click()
            break


@step('我在"(.*?)"中输入"(.*?)"')
def send_keys_for_element(step, element, text):
    element = world.element[element]
    world.driver.find_element(*element).send_keys(text)


@step('我获取"(.*?)"文本内容')
def get_element_text(step, element):
    element = world.element[element]
    world.text = world.driver.find_element(*element).text


@step('我点击文本"(.*?)"')
def click_text(step, text):
    element = (By.XPATH, '//*[text()="' + text + '"]')
    world.driver.find_element(*element).click()


@step('我点击一下文本"(.*?)"，如果文本不存在，我将点击"(.*?)"后再次尝试点击，最多(.*)次')
def click_text_retry(step, text, element, num):
    element_a = (By.XPATH, '//*[text()="' + text + '"]')
    element_b = world.element[element]
    for n in range(int(num)):
        try:
            world.driver.find_element(*element_a)
        except NoSuchElementException:
            world.driver.find_element(*element_b).click()
        else:
            world.driver.find_element(*element_a).click()
            break


# ````````````````````````````````````````常用检查点````````````````````````````````````````
@step('我比较文本与"(.*?)"是否相等')
def contrast_equal(step, text):
    assert world.text == text


@step('我检查元素"(.*?)"是否存在')
def check_element_exist(step, element):
    element = world.element[element]
    assert world.driver.find_elements(*element) == []


@step('我检查元素"(.*?)"是否不存在')
def check_element_no_exist(step, element):
    element = world.element[element]
    assert world.driver.find_elements(*element) != []


# ````````````````````````````````````````web常用操作封装````````````````````````````````````````
@step('我切换到浏览器第(.*)个页签')
def switch_tab(step, num):
    num = int(num)
    handles = world.driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    world.driver.switch_to.window(handles[num - 1])  # 跳转到第num个窗口


# 我点击下拉框xxx通过方式xxx选择xxx')
def select(way, element, *param):
    select = Select(world.driver.find_element(*element))
    value = param[0]
    if way == 'index':
        select.select_by_index(int(value))  # 索引,从0开始(1)
    elif way == 'value':
        select.select_by_value(value)  # option标签的一个属性值,并不是显示在下拉框的值("0")
    elif way == 'text':
        select.select_by_visible_text(value)  # option标签文本的值,是显示在下拉框的值(n"xxx")


@step('我移动鼠标至"(.*?)"位置')
def mouse_moves(step, element):
    element = world.element[element]
    ActionChains(world.driver).move_to_element(world.driver.find_element(*element)).perform()


@step('我点击键盘"(.*?)"按键(.*)次')
def keyboard(step, key, num):
    n = int(num)
    ac = ActionChains(world.driver)
    for i in range(n):
        if key == 'up':
            ac.send_keys(Keys.ARROW_UP)
        elif key == 'down':
            ac.send_keys(Keys.ARROW_DOWN)
        elif key == 'left':
            ac.send_keys(Keys.ARROW_LEFT)
        elif key == 'right':
            ac.send_keys(Keys.ARROW_RIGHT)
        elif key == 'enter':
            ac.send_keys(Keys.ENTER)
        elif key == 'backspace':
            ac.send_keys(Keys.BACKSPACE)
        elif key == 'tab':
            ac.send_keys(Keys.TAB)
        elif key == 'space':
            ac.send_keys(Keys.SPACE)
        elif key == 'f5':
            ac.send_keys(Keys.F5)
        elif key == 'ctrl+t':
            ac.send_keys(Keys.CONTROL + 'T')
    ac.perform()


# ````````````````````````````````````````app常用操作封装````````````````````````````````````````
# ````````````````````app设备滑屏操作````````````````````
# 获取屏幕尺寸
def get_screen_size():
    x = world.driver.get_window_size()['width']
    y = world.driver.get_window_size()['height']
    return x, y


@step('我操作手机设备，屏幕整体向"(.*?)"滑动(.*)次')
def device_screen_swipe(step, way, num):
    n = int(num)
    # 滑动方法
    size = get_screen_size()
    x1 = int(size[0] * 0.3)
    x2 = int(size[0] * 0.1)
    x3 = int(size[0] * 0.9)
    y1 = int(size[1] * 0.1)
    y2 = int(size[1] * 0.8)
    for i in range(n):
        time.sleep(0.3)
        if way == 'up':
            world.driver.swipe(x1, y2, x1, y1, 1000)
        elif way == 'down':
            world.driver.swipe(x1, y1, x1, y2, 1000)
        elif way == 'left':
            world.driver.swipe(x3, y1, x2, y1, 1000)
        elif way == 'right':
            world.driver.swipe(x2, y1, x3, y1, 1000)
        else:
            print('way参数错误')
    # 等待2s使滑动结束
    time.sleep(0.5)


# 屏幕滑动,至某元素出现
@step('我操作手机设备，屏幕整体向"(.*?)"滑动直至元素"(.*?)"出现')
def device_screen_swipe_custom(step, way, element):  # way只支持up、down、left、right
    element = world.element[element]
    while world.driver.find_elements(*element) == []:
        step.behave_as("""Given 我操作手机设备，屏幕整体向"{way}"滑动1次""".format(way=way))
        if world.driver.find_elements(*element) != []:
            break


# ````````````````````app设备权限授权````````````````````
@step('我操作手机设备，进行GPS授权')
def check_device_gps_btn(step):
    # 手机gps权限
    device_gps_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    try:
        element = world.driver.find_element(*device_gps_btn)
    except NoSuchElementException:
        pass
    else:
        element.click()


@step('我操作手机设备，进行短信授权')
def check_device_message_btn(step):
    # 手机短信权限
    device_message_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    try:
        element = world.driver.find_element(*device_message_btn)
    except NoSuchElementException:
        pass
    else:
        element.click()


@step('我操作手机设备，进行照片授权')
def check_device_photo_btn(step):
    # 手机照片权限
    device_photo_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    try:
        element = world.driver.find_element(*device_photo_btn)
    except NoSuchElementException:
        pass
    else:
        element.click()
        time.sleep(2)
        element.click()


@step('我操作手机设备，进行通讯录授权')
def check_device_phone_book_btn(step):
    # 手机通讯录权限
    device_phone_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    try:
        element = world.driver.find_element(*device_phone_btn)
    except NoSuchElementException:
        pass
    else:
        element.click()


@step('我操作手机设备，进行所有权限授权')
def check_device_permissions(step):
    step.behave_as("""
                Given 我操作手机设备，进行GPS授权
                And 我操作手机设备，进行短信授权
                And 我操作手机设备，进行照片授权
                And 我操作手机设备，进行通讯录授权
            """)


# ````````````````````app设备程序操作````````````````````
@step('我操作手机设备，进行拍照')
def click_device_photo_graph_action(step):
    # 相机元素(拍照按钮)
    device_photo_graph_type = (By.ID, 'com.android.camera2:id/shutter_button')
    # 相机元素(完成拍照按钮)
    device_photo_affirm_type = (By.ID, 'com.android.camera2:id/done_button')
    world.driver.find_element(*device_photo_graph_type).click()
    world.driver.find_element(*device_photo_affirm_type).click()


@step('我操作手机设备，选择通讯录第(.*)位')
def click_device_phone_book_action(step, num):
    n = int(num)
    device_phone_book_list_type = (By.ID, 'android:id/list')
    device_phone_book_list2_type = (By.CLASS_NAME, 'android.view.ViewGroup')
    device_phone_book_list3_type = (By.ID, 'com.android.contacts:id/cliv_data_view')
    device_phone_book_type = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/'
                                        'android.widget.FrameLayout[2]/android.widget.FrameLayout/'
                                        'android.widget.LinearLayout/android.widget.FrameLayout/'
                                        'android.widget.ListView/android.view.ViewGroup[' + str(n) + ']')
    # 因为contact_type中不能小于0所以使用是n要求大于0
    if n < 1:
        print('n不能小于0')
    else:
        try:
            world.driver.find_element(*device_phone_book_type)
        except NoSuchElementException:
            world.driver.find_element(*device_phone_book_list_type).find_elements(
                *device_phone_book_list2_type)[n].find_element(*device_phone_book_list3_type).click()
        else:
            world.driver.find_element(*device_phone_book_type).click()


# 日期控件年限滑动
def device_date_swipe(way, n):
    size = get_screen_size()
    x1 = int(size[0] * 0.3)
    y1 = int(size[1] * 0.715)
    y2 = int(size[1] * 0.8)
    for i in range(n):
        time.sleep(0.3)
        if way == 'up':
            world.driver.swipe(x1, y2, x1, y1, 1000)
        elif way == 'down':
            world.driver.swipe(x1, y1, x1, y2, 1000)
    world.driver.swipe(x1, y1, x1, y2, 1000)
    # 等待0.5s使滑动结束
    time.sleep(0.5)


# 日期插件选择(目前只选择年)
@step('我操作手机设备，选择日历向"(.*?)"滑动(.*)次并确定')
def click_device_date_action(step, way, n):
    device_date_affirm_type = (By.ID, 'android:id/button1')
    device_date_yes_type = (By.ID, 'android:id/date_picker_year')
    device_date_year_header_type = (By.ID, 'android:id/date_picker_header_year')
    device_date_type = (By.ID, 'android:id/date_picker_header_date')
    device_date_year_type = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                       'android.widget.FrameLayout/android.widget.LinearLayout/'
                                       'android.widget.FrameLayout/android.widget.FrameLayout/'
                                       'android.widget.DatePicker/android.widget.LinearLayout/'
                                       'android.widget.ViewAnimator/android.widget.ListView/android.widget.TextView[1]')
    device_date_year1_type = (By.ID, 'android:id/text1')

    world.driver.find_element(*device_date_year_header_type).click()
    time.sleep(2)
    device_date_swipe(way, int(n))  # 滑动年限/屏幕
    time.sleep(2)
    try:
        world.driver.find_element(*device_date_year_type)
    except NoSuchElementException:
        world.driver.find_element(*device_date_year1_type).click()
        world.driver.find_element(*device_date_affirm_type).click()
    else:
        world.driver.find_element(*device_date_year_type).click()
        world.driver.find_element(*device_date_affirm_type).click()


# ````````````````````````````````````````错误重试封装````````````````````````````````````````
@step('如果"(.*?)"仍然存在，我将重试点击最多(.*)次')
def click_error_retry_one(self, element, num):
    element = world.element[element]
    for n in range(int(num)):
        try:
            world.driver.find_element(*element)
        except NoSuchElementException:
            break
        else:
            world.driver.find_element(*element).click()


@step('如果"(.*?)"仍存在，我将重试点击"(.*?)"最多(.*)次')
def click_error_retry_two(self, element_a, element_b, num):
    element_a = world.element[element_a]
    element_b = world.element[element_b]
    for n in range(int(num)):
        try:
            world.driver.find_element(*element_a)
        except NoSuchElementException:
            pass
        else:
            world.driver.find_element(*element_b).click()


@step('如果"(.*?)"不存在，我将重试点击"(.*?)"最多(.*)次')
def click_error_retry_three(self, element_a, element_b, num):
    element_a = world.element[element_a]
    element_b = world.element[element_b]
    for n in range(int(num)):
        try:
            world.driver.find_element(*element_a)
        except NoSuchElementException:
            world.driver.find_element(*element_b).click()
        else:
            pass


@step('如果"(.*?)"仍然存在，我将重试点击直至不存在该元素')
def click_error_cycle_retry(self, element):
    element = world.element[element]
    while world.driver.find_elements(*element) != []:
        world.driver.find_element(*element).click()
        # 如果检查元素不存在,就终止循环
        if world.driver.find_elements(*element) == []:
            break
