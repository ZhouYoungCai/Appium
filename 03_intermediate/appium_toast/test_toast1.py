#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast():
    def setup(self):
        desire = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'deviceName': 'emulator-5554',
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'io.appium.android.apis.view.PopupMenu1',
            'automationName' : 'uiautomator2'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Search']").click()
        # print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, 'Clicked popup')]").text)