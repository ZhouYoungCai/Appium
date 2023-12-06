from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMultiNode:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(
            command_executor='http://10.1.1.104:4444',
            options=options
        )

    def test_multinode1(self):
        # 打开 baidu 页
        self.driver.get("http://www.baidu.com")
        # 向输入框中输入
        self.driver.find_element(By.ID, 'kw').send_keys("selenium")
        # 点击搜索框
        self.driver.find_element(By.ID, 'su').click()
        # 等待一秒
        sleep(1)
        # 断言输入内容在页面中
        assert "selenium" in self.driver.page_source

    def test_multinode2(self):
        # 打开 baidu 页
        self.driver.get("http://www.baidu.com")
        # 向输入框中输入
        self.driver.find_element(By.ID, 'kw').send_keys("appium")
        # 点击搜索框
        self.driver.find_element(By.ID, 'su').click()
        # 等待一秒
        sleep(1)
        # 断言输入内容在页面中
        assert "appium" in self.driver.page_source

    def test_multinode3(self):
        # 打开 baidu 页
        self.driver.get("http://www.baidu.com")
        # 向输入框中输入
        self.driver.find_element(By.ID, 'kw').send_keys("pytest")
        # 点击搜索框
        self.driver.find_element(By.ID, 'su').click()
        # 等待一秒
        sleep(1)
        # 断言输入内容在页面中
        assert "pytest" in self.driver.page_source

    def test_multinode4(self):
        # 打开 baidu 页
        self.driver.get("http://www.baidu.com")
        # 向输入框中输入
        self.driver.find_element(By.ID, 'kw').send_keys("requests")
        # 点击搜索框
        self.driver.find_element(By.ID, 'su').click()
        # 等待一秒
        sleep(1)
        # 断言输入内容在页面中
        assert "requests" in self.driver.page_source

    def test_multinode5(self):
        # 打开 baidu 页
        self.driver.get("http://www.baidu.com")
        # 向输入框中输入
        self.driver.find_element(By.ID, 'kw').send_keys("java")
        # 点击搜索框
        self.driver.find_element(By.ID, 'su').click()
        # 等待一秒
        sleep(1)
        # 断言输入内容在页面中
        assert "java" in self.driver.page_source

    def teardown_method(self):
        self.driver.quit()
