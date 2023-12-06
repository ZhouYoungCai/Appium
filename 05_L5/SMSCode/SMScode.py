"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import subprocess


class SMScode:

    @classmethod
    def get_by_ADB(cls):
        cmd = "adb shell am broadcast -a io.appium.settings.notifications"
        # 执行adb命令并返回结果
        lines = subprocess.Popen(cmd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 shell=True).stdout.readlines()
        # 对短信内容进行切片，获取最后一个验证码
        code = str(lines[1], 'utf-8').split("技】")[1].split("（企")[0].strip()
        return code