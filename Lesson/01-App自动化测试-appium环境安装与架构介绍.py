1、需要安装的软件
	1、java1.8版本，配置环境变量
	2、Android SDK，配置环境变量
	3、appium desktop
	4、python 3
	5、appium python client 
	安装软件地址：
	https://ceshiren.com/t/topic/2270
2、mobile自动化的方案
    IOS:calabash-ios,Frank,UIAutomation,ios-driver,KeepItFunction
	Android:calabash-android,MonkeyTalk,Robotium,UIAutomator,selendroid
3、自动化工具的选择
    单平台or多平台测试
	是否有多设备同时测试的场景
	不局限于测试环境，任何版本任何环境都可以测试
	最擅长哪种开发语言
	当前市面是否有满足项目需求的测试工具，是否需要二次开发
4、appium介绍
    appium是一个移动端的自动化测试框架，可用于测试原生应用，移动网页应用和混合应用，且是跨平台的。
	可用于IOS和Android操作系统。原生应用是指用Android或IOS编写的应用，移动网页应用是指网页应用
	类似于IOS中Safari应用或者Chrome应用或者类似浏览器的应用。
	混合应用是指一种包裹webview的应用，原生应用网页内容交互性的应用。
	重要的是appium是跨平台的。可以针对不同平台用一套api来编写脚本。
5、appium介绍
    跨语言：Java、python、nodejs等
	跨平台：Android、IOS、Windows、Mac
	底层多引擎可切换
	生态丰富，社区强大
6、appium设计理念
    webdriver是基于http协议的，第一连接会建立一个session会话，并通过post发送一个json告知服务端相关测试信息
	client/server设计模式
	    客户端通过webdriver json wire协议与服务端通讯
		多语言支持
	server可以放在任何地方
	服务端nodejs开发的http服务
	appium使用appium-xcuitest-driver来测试iPhone设备，
	其中需要安装facebook出的WDA(webdriver agent)来驱动IOS测试
7、appium生态工具
    adb：Android的控制工具，用于获取Android的各种数据和控制
	appium desktop:	内嵌了appium server和inspector的综合工具
	appium server：appium的核心工具，命令行工具
	appium client：各种语言的客户端封装库，用于连接appium server
	    python、Java、ruby、robotframework-appium
	AppCrawler:自动遍历工具
8、JDK安装与配置
    安装JDK（1.8版本）
	    官网下载地址：已下载
	安装（一直点下一步）完成，用默认路径即可
	配置环境变量
	    JAVA_HOME C:\Android\Java\jdk1.8.0_25  (注意这里的JAVA_HOME大写后面会用到)
		classpath .%JAVA_HOME\lib\dt.jar;%JAVA_HOME%\LIB\TOOLS.JAR;  (最前面加个点和分号.;)
		path  %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;
	检查Java环境是否配置好，进入命令行，输入：java -version或javac -version，呼出版本号信息即成功。
9、SDK安装与配置
    安装SDK
	   SDK就是个文件夹，下载之后需要手动更新，配上环境变量就可以使用，不需要安装
	配置Android SDK环境变量，如下：
	    ANDROID_HOME D:\adt-bundle-mac-x86_64-20140702\sdk
		PATH %ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools
	检查是否安装成功，cmd输出
	    adb回车或者adb shell ，然后回车
10、验证环境是否安装成功
    1、首先打开appium desktop,点击start server（不报错）
	2、其次准备一个安卓设备，真机或者模拟器（推荐mumu模拟器）
    3、模拟器连接到电脑
	4、adb devices 查看设备是否连接
	5、最后编写脚本，运行脚本，不报错
11、adb如何连接mumu模拟器
    命令窗口输入：adb connect 127.0.0.1:7555   ---连接mumu模拟器
	              adb connect 127.0.0.1:21503  ---连接逍遥模拟器
				  adb connect 127.0.0.1:62001  ---连接夜神模拟器
				  adb connect 127.0.0.1:54001  ---连接iTools模拟器
	检查连接的设备：adb devices
12、下载安装模拟器
    mumu 模拟器
	电脑开启VT（虚拟化技术）
	设置屏幕显示（720*1280）重启
	连接adb connect
	appium 第一个测试用例:https://ceshiren.com/t/topic/12652
		1、启动一个模拟器（比如：mumu模拟器）
		2、与模拟器建立连接
		【win版】
		adb connect 127.0.0.1:7555
		adb shell
		【mac版】
		adb kill-server && adb server && adb shell
		3、启动appium server
		最后：创建文件demo.py，执行python demo.py
		from appium import webdriver
		desired_caps={}
		desired_caps['platformName']='Android'
		desired_caps['platformVersion']='6.0'
		desired_caps['deviceName']='emulator-5554'
		# com.android.settings/com.android.settings.Settings
		desired_caps['appPackage']='com.android.settings'
		desired_caps['appActivity']='com.android.settings.Settings'
		driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
		print("启动【设置】应用")
		driver.quit()
