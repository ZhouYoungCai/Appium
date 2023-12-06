"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 导入 pip install appium-python-client
from appium import webdriver

# 创建一个字典，desirecapbility
caps = {}
caps["platformName"] = "Android"
# Android 包名和页面名，获取命令：
# mac/linux: adb logcat ActivityManager:I | grep "cmp"
# windows: adb logcat ActivityManager:I | findstr "cmp"
caps["appPackage"] = "io.appium.android.apis"
caps["appActivity"] = ".ApiDemos"
caps["deviceName"] = "emulator-5554"
# 创建driver ,与appium server建立连接，返回一个 session
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("OS")
el1.click()
el2 = driver.find_element_by_accessibility_id("Morse Code")
el2.click()
el3 = driver.find_element_by_id("io.appium.android.apis:id/text")
el3.clear()
el3.send_keys("ceshiren.com")
driver.back()
# 返回
driver.back()
# 回收session
driver.quit()
