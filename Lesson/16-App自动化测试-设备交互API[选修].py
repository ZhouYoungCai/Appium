1、目录
	测试过程中模拟来电，来短信
	模拟网络切换
	运行过程中获取系统日志
	截图
2、模拟来电和短信发送
	模拟器不能使用木木，可以用sdk自带的模拟器或者真机
	模拟来电：driver.make_gsm_call('13612312312', GsmCallActions.CALL)，需要导入GsmCallActions库
	模拟发短信：driver.send_sms('13612312312', 'hello appium apis')
	模拟网络设置：
	网络设置类别：driver.set_network_connection(connection_type: int)
    Sets the network connection type. Android only.

        Possible values:

            +--------------------+------+------+---------------+
            | Value (Alias)      | Data | Wifi | Airplane Mode |
            +====================+======+======+===============+
            | 0 (None)           | 0    | 0    | 0             |
            +--------------------+------+------+---------------+
            | 1 (Airplane Mode)  | 0    | 0    | 1             |
            +--------------------+------+------+---------------+
            | 2 (Wifi only)      | 0    | 1    | 0             |
            +--------------------+------+------+---------------+
            | 4 (Data only)      | 1    | 0    | 0             |
            +--------------------+------+------+---------------+
            | 6 (All network on) | 1    | 1    | 0             |
            +--------------------+------+------+---------------+

        These are available through the enumeration `appium.webdriver.ConnectionType`

        Args:
            connection_type: a member of the enum `appium.webdriver.ConnectionType`

        Return:
            int: Set network connection type
	截屏操作：self.driver.get_screenshot_as_file('./photos/img.png')
	进行手机录屏：
	只支持Android8.0以上版本，且部分手机如华为不支持
	self.driver.start_recording_screen()
	self.driver.stop_recording_screen()
3、具体代码
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestParam:
    def setup(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.main.view.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = "true"
        """当要输入中文时需要以下两个参数"""
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['resetKeyBoard']='true'
        # # 超时时间
        # desired_caps['adbExecTimeout'] = 500000
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        # 模拟打电话
        self.driver.make_gsm_call('13612312312', GsmCallActions.CALL)
        # 模拟发短信
        self.driver.send_sms('13612312312', 'hello appium apis')
        # 模拟网络设置，设置为飞行模式
        self.driver.set_network_connection(1)
        sleep(3)
        # 模拟网络设置，设置为数据模式
        self.driver.set_network_connection(4)
        # 获取截图并保存到路径中
        self.driver.get_screenshot_as_file('./photos/img.png')
        """
        进行录屏操作
        1.开始录屏
        2.停止录屏
        3.只支持Android8.0以上版本，且部分手机如华为不支持
        """
        self.driver.start_recording_screen()
        self.driver.stop_recording_screen()