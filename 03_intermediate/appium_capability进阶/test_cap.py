#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *

class TestSearch:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'hogwarts'
        desired_caps['udid'] = 'emulator-5554'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['dontStopAppOnReset'] =True
        desired_caps['app'] = '/Users/juanxu/Documents/霍格沃兹培训/录播课程/appium/测试demo/appium_capability进阶/xueqiu.apk'
        desired_caps['newCommandTimeout'] = 300
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibab")
        print(self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android')
              .get_attribute('class'))
        print(self.driver.page_source)
