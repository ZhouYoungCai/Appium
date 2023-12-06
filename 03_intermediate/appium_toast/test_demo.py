#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
import subprocess


platformversion = subprocess.getoutput("adb shell getprop ro.build.version.release")

class TestToast():
    def setup(self):
        desire = {

            'platformName' : 'android',
            'platformVersion' : platformversion,
            'deviceName' : 'emulator-5554',
            'appPackage' : 'io.appium.android.apis',
            'appActivity' : 'io.appium.android.apis.view.PopupMenu1',

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_toast(self):
        ele = self.driver.find_element_by_accessibility_id("Make a Popup!")
        ele.click()
        self.driver.find_element_by_xpath("//*[@text='Search1']").click()
        # print(self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element_by_xpath("//*[contains(@text, 'item Search')]").text)

        # self.driver.find_element_by_xpath("//*[@text='Search']").get_attribute("")
