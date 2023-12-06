"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from app_demo1.app_PODEMO.base.xueqiu_app import XueQiuApp
from app_demo1.app_PODEMO.page.search_result_page import SearchResultPage


class SearchPage(XueQiuApp):

    def input_searchcontent(self, searchkey):
        # input search content
        self.find_and_send(AppiumBy.ID,
                           "com.xueqiu.android:id/search_input_text", searchkey)
        return self

    def click_searchresult(self, text):
        # click 搜索结果
        self.find_and_click(AppiumBy.XPATH, f"//*[@text='{text}']")
        return SearchResultPage(self.driver)
