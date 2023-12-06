"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 导入 pip install appium-python-client
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestAppDemo:
    def setup(self):
        # 创建一个字典，desirecapbility
        caps = {}
        caps["platformName"] = "Android"
        # Android 包名和页面名，获取命令：
        # mac/linux: adb logcat ActivityManager:I | grep "cmp"
        # windows: adb logcat ActivityManager:I | findstr "cmp"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["deviceName"] = "emulator-5554"
        caps["noReset"] = "true"

        # 创建driver ,与appium server建立连接，返回一个 session
        # driver 变成self.driver 由局部变量变成实例变量，就可以在其它的方法中引用这个实例变量了
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 回收session
        self.driver.quit()

    def test_input(self):
        # el1 = self.driver.find_element_by_accessibility_id("OS")
        el1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OS")
        el1.click()
        # el2 = self.driver.find_element_by_accessibility_id("Morse Code")
        el2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Morse Code")
        el2.click()
        # el3 = self.driver.find_element_by_id("io.appium.android.apis:id/text")
        el3 = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/text")
        # 清除原有的内容
        el3.clear()
        el3.send_keys("ceshiren.com")
        el3.clear()
        # 手动制造关闭应用
        sleep(5)
        # 启动应用， 热启动，会进入到app 的首页
        self.driver.launch_app()
        result = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Accessibility").text
        # 断言
        assert result == "Accessibility"

    def test_seeking(self):
        """
        打开 demo.apk
        1. 点击 Animation 进入下个页面
        2. 点击 Seeking 进入下个页面
        3. 查看【RUN】按钮是否显示/是否可点击
        4. 查看【滑动条】是否显示/是否可用/是否可点击
        5. 获取【滑动条】长度
        6. 点击【滑动条】中心位置
        :return:
        """
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Seeking").click()
        # 3. 查看【RUN】按钮是否显示/是否可点击
        run_element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Run")
        run_is_displayed = run_element.is_displayed()
        run_is_clickable = run_element.get_attribute("clickable")
        print(f"【run】按钮是否可见：{run_is_displayed},是否可点击:{run_is_clickable}")
        # 4. 查看【滑动条】是否显示/是否可用/是否可点击
        seekbar_element = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/seekBar")
        seekbar_displayed = seekbar_element.is_displayed()
        seekbar_enabled = seekbar_element.is_enabled()
        seekbar_clickable = seekbar_element.get_attribute("clickable")
        print(f"seekbar 滑动条 是否可见：{seekbar_displayed},"
              f"是否可用：{seekbar_enabled},"
              f"是否可点击：{seekbar_clickable}")
        # 5.获取【滑动条】长度
        seekbar_size = seekbar_element.size
        width = seekbar_size.get("width")
        height = seekbar_size.get("height")
        print(f"seekbar 的长度：{width}")

        seekbar_location = seekbar_element.location
        x = seekbar_location.get("x")
        y = seekbar_location.get("y")
        # 6.点击【滑动条】中心位置
        seekbar_centerx = x + width / 2
        seekbar_centery = y
        self.driver.tap([(seekbar_centerx, seekbar_centery)])
        sleep(5)
