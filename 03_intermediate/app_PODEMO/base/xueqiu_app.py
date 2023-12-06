"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# app 相关的操作： 雪球应用的start 启动，重启restart, 停止 stop
from appium import webdriver

from app_demo1.app_PODEMO.base.base_page import BasePage


class XueQiuApp(BasePage):
    def start(self):
        # 启动app
        if self.driver == None:
            print("driver == None")
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            # mac: adb logcat ActivityManager:I | grep "cmp"
            # win: adb logcat ActivityManager:I | findstr "cmp"
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
            desired_caps['noReset'] = 'true'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)
        else:
            # 直接启动app
            print("复用driver")
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        from app_demo1.app_PODEMO.page.main_page import MainPage

        return MainPage(self.driver)
