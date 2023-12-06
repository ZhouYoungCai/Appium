"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from app_demo1.app_PODEMO.base.xueqiu_app import XueQiuApp
from app_demo1.app_PODEMO.page.search_page import SearchPage


class MainPage(XueQiuApp):
    _SEARCH_BOX_ELEMENT = (AppiumBy.ID,
                           "com.xueqiu.android:id/tv_search")

    def click_search(self):
        # click searchbox 搜索框
        self.find_and_click(*self._SEARCH_BOX_ELEMENT)

        # com.xueqiu.android:id/tv_search
        return SearchPage(self.driver)
