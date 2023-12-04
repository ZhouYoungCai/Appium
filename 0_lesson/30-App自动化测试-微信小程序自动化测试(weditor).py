文章链接：https://www.jianshu.com/p/bebe22d1af3b
1、测试代码
	def setup(self):
		self.desire_cap= {
			"platformName": "Android",
			"deviceName": "wechat",
			"appPackage": "com.tencent.mm",
			"appActivity": ".ui.LauncherUI",
			"noReset": "true",
			'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
		}
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
		self.driver.implicitly_wait(10)

	def teardown(self):
		self.driver.quit()

	def test_demo(self):
		self.driver.find_element_by_xpath("//*[@text='通讯录']")
		size = self.driver.get_window_size()
		width = size.get("width")
		height = size.get("height")
		self.driver.swipe((width / 2), int((height * 0.2)), (width / 2), (height * 0.8), 2000)
		self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/gam' and @text='雪球']").click()
		sleep(5)
		print(self.driver.contexts,'第一次打印')
		self.driver.find_element_by_xpath("//*[@content-desc='搜索股票信息/代码']/..").click()
		self.driver.find_element_by_xpath('//*[@text="请输入股票名称/代码"]').send_keys("阿里巴巴")
		text = self.driver.find_element_by_xpath('//*[@content-desc="阿里巴巴"]')
		assert text
	模拟器：Genymotion
	系统版本：8.1
	微信版本：7.0.15
	小程序：雪球
2、步骤
	获取小程序进程号（打开小程序）
		mac：adb shell dumpsys activity top| grep ACTIVITY
		win：adb shell dumpsys activity top| findstr ACTIVITY
		image
	获取androidProcess
		adb shell ps 9552
		image
3、定位
	请使用 weditor 进行定位
	https://github.com/alibaba/web-editor
	使用chrome inspect 或者UC开发者工具定位时，解析元素是把页面解析为 html 页面，
		使用 weditor，则会把页面解析为原生页面，而Appium在操作原素时，也是把页面解析成了原生去操作的（切webview除外）
	接下来就可以按照原生的页面去愉快的操作元素啦
4、解疑
	chromeOptions：
	Appium官方预留了chromeOptions选项，在capability里可以添加这个参数来自定义配置ChromeDriver 会话的选项
		image
	androidProcess：设置webview的进程名字，如果没有设置这个参数，则默认为app的包名
5、注意事项
	不要去切 webview！！！
	不要去切 webview！！！
	不要去切 webview！！！
	参考文档：
		http://appium.io/docs/en/writing-running-appium/caps/
		https://sites.google.com/a/chromium.org/chromedriver/capabilities
		https://sites.google.com/a/chromium.org/chromedriver/getting-started/getting-started---android
	微信历史版本下载：
		https://weixin.qq.com/cgi-bin/readtemplate?t=weixin_faq_list
