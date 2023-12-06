"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains


class TestXueQiu:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_price(self):
        search_key = "alibaba"
        # 点击搜索框，进入搜索页面
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        # 输入搜索内容
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text"). \
            send_keys(search_key)
        # 点击【阿里巴巴】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']").click()
        # 获取股票 【BABA】 对应的股票价格
        current_element = self.driver.find_element(MobileBy.XPATH,
                                                   "//*[@text='BABA']/../../..//*[contains(@resource-id, 'current_price')]")
        current_price = float(current_element.text)
        print(f"当前股票 {search_key} 的股票价格为：{current_price}")
        from hamcrest import assert_that, close_to
        expect_price = 110
        # 断言，价格 与期望股票价格上下浮动 10%
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))

    def get_time(self):
        # 获取前面时间
        t = time.localtime(time.time())
        cur_time = time.strftime("%Y-%m-%d_%H:%M:%S", t)
        print(f"当前时间为：{cur_time}")
        return cur_time

    # @pytest.mark.skip
    def test_search(self):
        '''使用 xpath 定位'''
        logging.info("搜索用例")
        element = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tv_search']")
        search_enabled = element.is_enabled()
        logging.info(f"搜索框的文本：{element.text}，搜索框的坐标：{element.location}，搜索框的size：{element.size}")

        if search_enabled == True:
            logging.info("点击搜索框")
            element.click()
            logging.info("向搜索框中输入内容：alibaba")
            self.driver.find_element(MobileBy.XPATH,
                                     "//*[@resource-id='com.xueqiu.android:id/search_input_text']"). \
                send_keys("alibaba")

            alibaba_element = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")

            # alibaba_element.is_displayed()
            displayed = alibaba_element.get_attribute("displayed")
            logging.info("搜索结果是否处于显示状态 ：" + displayed)
            logging.info("搜索结果页的页面源码为：" + self.driver.page_source)
            self.driver.save_screenshot("./image/result.png")
            assert displayed == "true"

    def test_search1(self):
        '''使用css selector 定位'''
        print(f"开始时间：{self.get_time()}")
        # element = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search")
        element = self.driver.find_element(AppiumBy.CSS_SELECTOR, "#com\.xueqiu\.android\:id\/tv_search")
        search_enabled = element.is_enabled()
        print(f"搜索框的文本：{element.text}，搜索框的坐标：{element.location}，搜索框的size：{element.size}")

        if search_enabled == True:
            element.click()
            self.driver.find_element(AppiumBy.CSS_SELECTOR,
                                     "#com\.xueqiu\.android\:id\/search_input_text"). \
                send_keys("alibaba")
            # alibaba_element = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")

            alibaba_element = self.driver.find_element(AppiumBy.CSS_SELECTOR, "*[text='阿里巴巴']")
            # alibaba_element.is_displayed()
            displayed = alibaba_element.get_attribute("displayed")
            print(displayed)
            assert displayed == "true"
        print(f"结束时间：{self.get_time()}")

    def test_search2(self):
        '''使用 android uiautomator 定位'''
        print(f"开始时间：{self.get_time()}")
        # element = self.driver.find_element(AppiumBy.ID, "tv_search")
        # element = self.driver.find_element(AppiumBy.CSS_SELECTOR, "*[resource-id='com.xueqiu.android:id/tv_search']")
        element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiSelector().resourceId("com.xueqiu.android:id/tv_search")')
        self.driver.save_screenshot()
        search_enabled = element.is_enabled()
        print(f"搜索框的文本：{element.text}，搜索框的坐标：{element.location}，搜索框的size：{element.size}")

        if search_enabled == True:
            element.click()
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                     'new UiSelector().resourceId("com.xueqiu.android:id/search_input_text")').send_keys(
                "alibaba")
            # alibaba_element = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")

            alibaba_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("阿里巴巴")')
            # alibaba_element.is_displayed()
            displayed = alibaba_element.get_attribute("displayed")
            print(displayed)
            assert displayed == "true"
        print(f"结束时间：{self.get_time()}")
