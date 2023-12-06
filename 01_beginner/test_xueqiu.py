"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestSearch:
    def setup(self):
        # 创建一个字典，desirecapbility
        caps = {}
        caps["platformName"] = "Android"
        # Android 包名和页面名，获取命令：
        # mac/linux: adb logcat ActivityManager:I | grep "cmp"
        # windows: adb logcat ActivityManager:I | findstr "cmp"
        # com.xueqiu.android/.view.WelcomeActivityAlias
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["deviceName"] = "emulator-5554"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(20)

    def teardown(self):
        # 关闭应用
        self.driver.quit()

    def test_search(self):
        """
        1. 判断搜索框的是否可用,并查看搜索框 name 属性值，并获取搜索框坐标，以及它的宽高
        2. 点击搜索框
        3. 向搜索框输入:alibaba
        4. 判断【阿里巴巴】是否可见
            如果可见，打印“搜索成功”
            如果不可见，打印“搜索失败
        :return:
        """
        # 1. 判断搜索框的是否可用,并查看搜索框 name 属性值，并获取搜索框坐标，以及它的宽高
        search_key = "alibaba"
        searchbox_ele = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/home_search")
        # 先判断一下搜索框是否可用
        if searchbox_ele.is_enabled():
            searchbox_text = searchbox_ele.text
            searchbox_location = searchbox_ele.location
            searchbox_size = searchbox_ele.size
            print(f"首页搜索框的 text：{searchbox_text}")
            print(f"首页搜索框的 location坐标为：{searchbox_location}")
            print(f"首页搜索框的 size 宽高：{searchbox_size}")
            # 2. 点击搜索框
            searchbox_ele.click()
            # 3. 向搜索框输入:alibaba
            self.driver.find_element(AppiumBy.ID,
                                     "com.xueqiu.android:id/search_input_text").send_keys(search_key)
            # 4. 判断【阿里巴巴】是否可见
            #             如果可见，打印“搜索成功”
            #             如果不可见，打印“搜索失败
            #
            alibaba_element = self.driver.find_element(AppiumBy.XPATH, "//*[@text='阿里巴巴']")
            result = alibaba_element.is_displayed()
            # print(result)
            if result == True:
                print("搜索成功")
            else:
                print("搜索失败")
            assert result == True
        else:
            print("搜索框不可用")
            assert False
