"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https:#ceshiren.com/t/topic/15860'
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from L5.SMSCode.SMScode import SMScode


class TestSMS:
    def setup_class(self):
        self.desire_cap = {
            "platformName": "Android",
            "appium:deviceName": "31030c8d",
            "appium:automationName": "Appium",
            "appium:appPackage": "com.tencent.wework",
            "appium:appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    def test_login_by_ADB(self):
        # 勾选已同意
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='已阅读并同意 软件许可及服务协议 和 隐私政策']/../android.widget.ImageView").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='已阅读并同意 软件许可及服务协议 和 隐私政策']/../android.widget.ImageView").click()
        # 点击手机号登录
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手机号登录']").click()
        # 输入手机号
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手机号']").send_keys("13926528314")
        # 点击下一步
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='下一步']").click()
        sleep(10)
        # 获取验证码
        code = SMScode.get_by_ADB()
        # 上划关闭通通知栏
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        self.driver.swipe((width / 2), int((height * 0.3)), (width / 2), (height * 0.1), 2000)
        sleep(5)
        # 输入验证码
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='验证码']").send_keys(code)
        # 点击下一步
        sleep(5)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='下一步']").click()
        # 验证是否登录成功
        text = self.driver.find_element(AppiumBy.XPATH, "//*[@text='选择工作身份']").get_attribute("text")
        assert "选择工作身份" == text
