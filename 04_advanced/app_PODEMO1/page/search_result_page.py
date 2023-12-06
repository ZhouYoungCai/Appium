"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.appiumby import AppiumBy

from app_demo1.app_PODEMO1.base.xueqiu_app import XueQiuApp


class SearchResultPage(XueQiuApp):

    def goto_stock_tab(self):
        # click 股票
        self.find_and_click(AppiumBy.XPATH, "//*[@text='股票']")
        return self

    def get_price(self, stock_num):
        # 找到阿里巴巴所对应的股票价格
        current_price = self.find_and_gettext(AppiumBy.XPATH,
                                              f"//*[@text='{stock_num}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        return float(current_price)
