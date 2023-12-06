#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time
import pytest
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.common.MainActivity',
            # 'browserName':'Chrome',
            'deviceName':'192.168.56.101:5555',
            'noReset' :'true',
            # 'deviceName': 'emulator-5554',
            'skipServerInstallation' :'true',
            # 'showChromedriverLog':True,
            'chromedriverExecutableDir':'/Users/juanxu/Documents/mychromedriver/all',
            'chromedriverChromeMappingFile': '/Users/juanxu/Documents/霍格沃兹培训/录播课程/appium/测试demo/appium_webview_lu/mapping.json'

            # 'chromedriverExecutable': '/Users/juanxu/Documents/chromedriver'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        pass
        # self.driver.quit()

    def test_webview(self):
        # 点击交易
        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()
        A_locator = (MobileBy.XPATH, '//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')
        print(self.driver.contexts)
        # 切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击'A股开户'
        print(self.driver.window_handles)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        kaihu_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)

        # 显式等待 ，等待
        phonenumber_locator = (MobileBy.ID, 'phone-number')
        WebDriverWait(self.driver,60).until(expected_conditions.element_to_be_clickable(phonenumber_locator))
        # 输入用户名和验证码，点击立即开户
        self.driver.find_element(*phonenumber_locator).send_keys("13810100202")
        self.driver.find_element(MobileBy.ID, 'code').send_keys("1234")
        self.driver.find_element(MobileBy.CSS_SELECTOR, 'body > div > div > div.form-wrap > div > div.btn-submit').click()











