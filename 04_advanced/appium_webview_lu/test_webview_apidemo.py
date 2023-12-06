#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time
import pytest
from time import sleep

from appium.webdriver.common.mobileby import MobileBy


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'io.appium.android.apis.ApiDemos',
            # 'browserName':'Chrome',
            'deviceName':'192.168.56.101:5555',
            'noReset' :'true',
            # 'deviceName': 'emulator-5554',
            'chromedriverExecutable': '/Users/juanxu/Documents/chromedriver'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        pass
        # self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        webview = "WebView"
        print(self.driver.contexts)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}")'
                                                        '.instance(0));').click()
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'i has no focus').send_keys("this is a test string")
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'i am a link').click()
        # print(self.driver.page_source)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, 'i_am_a_textbox').send_keys("this is a test string use chrome inspect")
        self.driver.find_element(MobileBy.ID,'i am a link').click()
        print(self.driver.page_source)
        self.driver.find_element_by_android_uiautomator()
        self.driver.find_element_by_ios_predicate()
        self.driver.find_element_by_css_selector()
        self.driver.find_element_by_xpath()









