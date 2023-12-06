"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# pip install uiautomator2
import uiautomator2 as u2


class TestContact:
    app_package = "com.tencent.wework"
    app_activity = ".launch.LaunchSplashActivity"

    def setup_class(self):
        # 连接设备+ 设置隐式等待
        self.d = u2.connect()
        self.d.implicitly_wait(10)

    def setup(self):
        # 定义监控
        self.d.watcher.when("//*[@text = '同意']").click()
        # 开始监控
        self.d.watcher.start()
        # 关闭所有应用
        # self.d.app_stop_all()
        # 启动应用
        self.d.app_start(self.app_package, self.app_activity, wait=True)

    def teardown(self):
        # 关闭应用
        self.d.app_stop(self.app_package)
        # 关闭监控
        self.d.watcher.stop()

    def test_addcontact(self):
        """
        点击【通讯录】
        点击【添加成员】
        点击【手动输入添加】
        等待【保存】显示出来
        输入姓名【hogwarts】
        输入手机号【13100000000】
        点击【保存】
        验证添加成功
        :return:
        """
        self.d(text="通讯录").click()
        self.d(text="添加成员").click()
        self.d(text="手动输入添加").click()
        # 等待【保存】显示出来
        self.d(text="保存").wait(timeout=3.0)
        # 输入姓名【hogwarts】
        self.d(textContains="姓名"). \
            sibling(className="android.widget.EditText"). \
            set_text("hogwarts")
        # 输入手机号【13100000000】
        self.d(textContains="手机"). \
            sibling(className="android.widget.RelativeLayout"). \
            child(className='android.widget.EditText').set_text("13111111113")
        self.d(text="保存").click()
        # 验证添加成功
        self.d.toast.get_message(5, 5, "添加成功")
