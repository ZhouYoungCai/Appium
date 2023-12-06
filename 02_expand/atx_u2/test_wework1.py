"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from time import sleep

import uiautomator2 as u2


class TestU2:

    def setup(self):
        # 连接设备
        self.d = u2.connect()
        self.d.app_start("com.tencent.wework",
                         ".launch.LaunchSplashActivity", wait=True)
        self.d.implicitly_wait(10)

    def test_addcontact(self):
        self.d(text="通讯录").click()
        self.d(text="添加成员").click()
        self.d(text="手动输入添加").click()
        self.d.send_keys("hogwarts", clear=True)
        self.d(resourceId="com.tencent.wework:id/h32").click()
        self.d.send_keys("13100000000", clear=True)

    # def test_demo1(self):
    #     # 设备信息
    #     print(self.device.info)
    #     # 设备详细信息
    #     print(self.device.device_info)
    #     print(self.device.window_size())
    #
    # def test_demo2(self):
    #     self.device.app_start("com.tencent.wework",
    #                           ".launch.LaunchSplashActivity",wait=True)
    #     print(self.device.current_app)
    #     print(self.device.app_list_running())
    #     sleep(2)
    #     self.device.app_stop("com.tencent.wework")
