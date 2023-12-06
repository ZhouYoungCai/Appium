"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

## 基本的方法，driver, find ，click,swipe。。。
import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from app_demo1.app_PODEMO1.base.black_handle import black_wrapper


class BasePage:
    black_list = [(AppiumBy.ID, "com.xueqiu.android:id/iv_close")]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # def find(self, by, locator):
    #     try:
    #         return self.driver.find_element(by, locator)
    #     except Exception as e:
    #         print("未找到")
    #         for e in self.black_list:
    #             print(f"遍历黑名单：{e}")
    #             eles = self.driver.find_elements(*e)
    #             # sleep(1)
    #             if len(eles) >0:
    #                 eles[0].click()
    #                 return self.find(by,locator)
    #         raise e
    # def find(self, by, locator):
    #     try:
    #         return self.driver.find_element(by, locator)
    #     except Exception as e:
    #
    #         for black in self.black_list:
    #             eles = self.driver.find_elements(*black)
    #             if len(eles) > 0:
    #                 eles[0].click()
    #                 return self.find(by, locator)
    #         raise e

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def find_and_gettext(self, by, locator):
        return self.find(by, locator).text

    def screenshot(self, name):
        # 截图
        self.driver.save_screenshot(name)

    def get_time(self):
        t = time.localtime(time.time())
        cur_time = time.strftime("%Y-%m-%d_%H_%M_%S", t)
        print(f"当前时间为：{cur_time}")
        return cur_time
