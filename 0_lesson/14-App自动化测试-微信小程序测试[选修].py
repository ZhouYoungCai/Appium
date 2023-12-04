链接：https://www.jianshu.com/p/15c9560d0fcd
1、小程序的运行环境
    运行环境            逻辑层                  渲染层
	IOS                 JavaScriptCore          WKwebview
	安卓                V8                      chromium定制内核
	小程序开发者工具    NWJS                    chromewebview
2、小程序的运行环境 
    微信小程序运行在多种平台上：IOS（iPhone/iPad）微信客户端，Android微信客户端，PC微信客户端，MAC微信客户端和用于调试的微信开发者工具。
	各平台脚本执行环境以及用于渲染非原生组件的环境是各不相同的：
	    在IOS上，小程序逻辑层的javascript代码运行在JavaScriptcore中，
		视图层是由WKWwebview来渲染的，环境有IOS12/IOS13等
		在Android上，小程序逻辑层的JavaScript代码运行在V8中，
		视图层由自研XWeb引擎基于mobile chrome内核来渲染。
		在开发者工具上，小程序逻辑层的JavaScript代码是运行在NW.js中，视图层是由WKWwebview来渲染的，环境有IOS12/IOS13等
		chromium webview来渲染的
	平台差异：
	    尽管各运行环境是十分相似的，但是还是有些许区别
		    JavaScript语法和API支持不一致，语法上开发者可以通过开启ES6和ES5的功能来规避，
			此外，小程序基础库内置了必要的polyfill,来弥补API差异
			WXSS渲染表现不一致：尽管可以通过开启样式补全来规避大部分的问题，
			还是建议开发者需要在IOS和Android上分别检查小程序的真实表现。
		开发者工具仅供调试使用，最终的表现以客户端为准。
3、微信小程序调试开关
    微信每个版本都很善变
	    可手工开启调试开关
		默认关闭了调试开关而且无法开启
		默认开启调试开关
	手工开启办法：
	    文件传输助手发送
		debugtbs.qq.com
		debugx5.qq.com
		打开微信小程序调试开关
4、微信小程序自动化测试的关键步骤
    设置Chromedriver正确版本
	设置chrome option传递给Chromedriver
	使用adb proxy解决 fix Chromedriver的bug
5、微信小程序自动化测试
	微信小程序的自动化测试，目前有两种。
		一、基于微信官方的SDK进行微信小程序的自动化测试
			微信小程序自动化 SDK 的缺点：
			从官网提供的代码示例来看，微信的这套体系主要用于研发自测
			微信的研发对自动化测试理解不到位，大量的 wait，实用性不高
			需要在已有的 WebSocket 体系上做二次封装对接 Appium
			希望微信可以重视这块的测试支持改进
			微信官方网址： https://developers.weixin.qq.com/miniprogram/dev/devtools/auto/
		二、基于webview利用uiautomator原生定位实现的微信小程序的自动化测试
			Appium 使用Uiautomator2定位可以识别内部WebView组件
			缺点：
			元素定位符不够精确，content-desc、resource-id 多数都没有
			NoReset 默认为 false，会默认清空微信聊天记录，所以请使用测试机测试帐号
			各版本情况：
			微信6.x版本支持基于WebView自动化测试（曾经这个方案是最好用的，Appium 默认支持）
			7.x改版后默认已经无法使用基于 WebView 的自动化
			7.x + root强行开启 WebView debug + Appium hack
			微信调试开关
			文件传输助手发送：debugtbs.qq.com或者debugx5.qq.com
			注意事项：
			WebView 开关/ x5内核调试开关
			x5内核版本低，需要低版本的ChromeDriver对应（WebView 版本和 ChromeDriver 版本对应问题 ）
			低版本的ChromeDriver在高版本7.x以上的Android手机上有Bug（低版本ChromeDriver需要修复 ps 命令的Bug ）
			ChromeOptions 选项需要填写AndroidProcess
			Context API有一定的延迟需要等待
		代码编写思路
			参考其他博主博文：https://www.cnblogs.com/yyoba/p/9455519.html
			参考开源项目：https://github.com/richshaw2015/wxapp-appium
6、为什么有些手机无法自动化微信小程序
		低版本的chromedriver在高版本的手机上有bug
		chromedriver与微信定制的chrome内核实现上有问题
	解决方案：fix it
		chromedriver没有使用adb命令，而是使用了adb协议
		参考提到的adb proxy源代码
		adb proxy
		mitmdump 
		-p 5038 
		--rawtcp 
		--mode reverse:http://localhost:5037/ 
		-s adb_proxy.py
    参考帖子：https://ceshiren.com/t/topic/3394
7、adb proxy 介绍
	shell mock技术
	    用于欺骗adb和appium，选择合适的chromedriver版本。个人使用可以先简单使用
		chromedriverExecutable代替
	协议mock adb proxy实现
		运行命令
		mitmdump -p 5038 --rawtcp --mode reverse:http://localhost:5037 -s tcp.py
8、辅助小程序测试的adb_proxy.py
"""
mitmdump -p 5038 --rawtcp --mode reverse:http://localhost:5037/ -s adb.py
"""
from mitmproxy.utils import strutils
from mitmproxy import ctx
from mitmproxy import tcp

def tcp_message(flow: tcp.TCPFlow):
    message = flow.messages[-1]
    old_content = message.content
    #message.content = old_content.replace(b"foo", b"bar")
    message.content = old_content.replace(b"@webview_devtools_remote_", b"@.*.*.*._devtools_remote_")

    ctx.log.info(
        "[tcp_message{}] from {} to {}:\n{}".format(
            " (modified)" if message.content != old_content else "",
            "client" if message.from_client else "server",
            "server" if message.from_client else "client",
            strutils.bytes_to_escaped_str(message.content))
    )
9、运行结果
	mitmdump -p 5038 --rawtcp --mode reverse:http://localhost:5037/ -s /tmp/adb.py
		Proxy server listening at http://*:5038
		127.0.0.1:58593: clientconnect
		127.0.0.1:58593 -> tcp -> localhost:5037 [tcp_message] from client to server:
		000chost:version
		127.0.0.1:58593 <- tcp <- localhost:5037
		[tcp_message] from server to client:
		OKAY00040029
		127.0.0.1:58593: clientdisconnect
		127.0.0.1:58596: clientconnect
		127.0.0.1:58596 -> tcp -> localhost:5037
		[tcp_message] from client to server:
		000chost:devices
		127.0.0.1:58596 <- tcp <- localhost:5037
		[tcp_message] from server to client:
		OKAY0000
		127.0.0.1:58596: clientdisconnect
10、基本capability设置
	DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
	desiredCapabilities.setCapability( capabilityName: "platformName",value:"android");
	desiredCapabilities.setCapability( capabilityName:"deviceName",value:"InsaneLoafer" );
	desiredCapabilities.setCapability( capabilityName: "appPackage",value: "com.tencent.mm")
	desiredCapabilities.setCapability( capabilityName:"appActivity" ,value:"com .tencent.m.ui.LauncherUI");
	desiredCapabilities.setCapability( capabilityName: "unicodeKeyboard",value:"true");
	desiredCapabilities.setCapability( capabilityName: "resetKeyboard",value: "true");
	##高危操作，如果设置错误，聊天记录会被清空，建议使用小号测试
	desiredCapabilities.setCapability( capabilityName: "noReset",value: "true");
11、chromedriver版本设置
	//第一步:设置正确的chromedriver
	//简单粗暴的解决方案
	desiredCapabilities.setCapability(capabilityName: "chromedriveExecutable",
			value: " /chromedniver/chromednivers/ chromedriver_78.0.3904.11");
	desiredCapabilities.setCapability( "chcomedrivecExecutable",
		"/chromedrcivec/chcomedrivers/chromedciver._2.23");
	//完善的版本选择方案，不过会优先找android webview默认实现
	desiredCapabilities.setCapability( "chromedcivecExecutableDir",
		"/ Users/seveniruby/projects/chcomedrivec/chromedcivecs");
	desiredCapabilities.setCapability( "chromedrciverChromeMappingFile",
		"/Users/seveniruby/projects/Java3/src/main/resources/mapping.json" );
	//打印更多chromedriver的log方便定位问题
	desiredCapabilities.setCapability( capabilityName: "showChromedriverLog", value: true);
12、chromedriver参数配置
	//第二步:设置chromeoption传递给chromedriver
	//因为小程序的进程名跟包名不一样，需要加上这个参数
	chromeOptions chromeOptions = new ChromeOptions();
	chromeOptions.setExperimentalOption( name: "androidPrgcess",value: "com.tencent.mm:appbrand0");
	desiredCapabilities.setCapability( "goog:chromeOptions", chromeOptions);
	//必须得加上，因为默认生成browserName=chrome的设置，需要去掉
	desiredCapabilities.setCapability( capabilityName: "browserName",value:"");
13、使用adb proxy
	/第三步:设置adb proxy
	//通过自己的adb代理修复chromedriver的bug并解决@xweb_devtools_remote的问题
	desiredCapabilities.setCapability( capabilityName: "adbPort",value: "5038");
14、项目实战--需要切换到可视化窗口--具体代码
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from appium import webdriver
from selenium.webdriver import ActionChains, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestwXMicro:
    # 为了演示方便,未使用page object模式
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "InsaneLoafer"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        caps["noReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["chromedriverExecutable"] = '/projects/chromedriver/chromedrivers/chromedriver_78.0.3904.11'
        # options = ChromeOptions()
        # options.add_experimental_option('androidProcess', 'com.tencent.mm:appbrand0')
        caps["chromeOptions"] = {
            "androidProcess": "com.tencent.mm: appbrand0"
        }
        caps['adbPort'] = 5038
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

    def test_search(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.1)
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
        self.driver.find_element(By.XPATH, "//*[@text='取消']")
        self.driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(By.XPATH, "//*[@text='自选']")

        print(self.driver.contexts)

        # 进入webview
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.implicitly_wait(10)
        self.find_top_window()

        # css定位
        self.driver.find_element(By.CSS_SELECTOR, "[src*= stock_add]").click()  # 等待新窗口
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # 输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys("alibaba").perform()
        # 点击
        self.driver.switch_to.context("WEBVIEW_xweb")
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item").click()


    def find_top_window(self):
        """
        切换到可视化窗口的函数
        :param driver:
        :return:
        """
        for window in self.driver.window_handles:
            print(window)

            if ":VISIBLE" in self.driver.title:
                print("find")
                print(self.driver.title)
                return True
            else:
                self.driver.switch_to.window(window)
        return False