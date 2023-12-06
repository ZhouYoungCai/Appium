"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSingleNode:
    def setup_method(self):
        # 创建Options ,新版本DesireCapability已弃用
        options = webdriver.EdgeOptions()
        # 通过URL和options 创建一个远程的连接
        # client 发送请求，要发送给selenium grid hub 结点， hub 结点会将请求分发到对应的node

        self.driver = webdriver.Remote(
            command_executor='http://10.1.1.104:4444',
            options=options
        )

    def test_singlenode1(self):
        # 打开 baidu 页
        self.driver.get("http://www.baidu.com")
        # 向输入框中输入
        self.driver.find_element(By.ID, 'kw').send_keys("firefox")
        # 点击搜索框
        self.driver.find_element(By.ID, 'su').click()
        # 等待一秒
        sleep(1)
        # 断言输入内容在页面中
        assert "firefox" in self.driver.page_source

    def teardown_method(self):
        self.driver.quit()
