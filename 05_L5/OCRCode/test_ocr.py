"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from L5.OCRCode.ocr_code import OcrCode


class TestCode:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # 打开页面
        self.driver.get("https://vip.ceshiren.com/#/ui_study/code")

    def teardown_class(self):
        self.driver.quit()

    def test_code(self):
        # 获取验证码图片链接
        img_url = self.driver.find_element(By.CSS_SELECTOR, ".code1:nth-child(2) img").get_attribute("src")
        # 获取验证码内容
        code = OcrCode.get_by_ocr(img_url)
        # 输入验证码
        self.driver.find_element(By.CSS_SELECTOR, ".code1:nth-child(2) input").send_keys(code)
        # 点击确定
        self.driver.find_element(By.CSS_SELECTOR, ".code1:nth-child(2) button").click()
        # 断言验证码是否正确
        sleep(1)
        text = self.driver.find_element(By.CSS_SELECTOR, ".el-message p").text
        print(text)
        assert text == "验证成功"
