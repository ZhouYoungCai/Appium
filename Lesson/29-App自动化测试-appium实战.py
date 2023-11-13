1、目录
	知识点梳理
	测试流程
	知识点练习
	业务分析
	用例设计
	编写用例
	练习题点评与解析
2、App 测试的时代背景
	按月发布->按周发布->按小时发布
	多端发布: Android、iOS、微信小程序、h5
	多环境发布: 联调环境、测试环境、预发布环境、线上环境
	多机型发布: 众多设备型号、众多系统版本
	多版本共存: 用户群体中存在多个不同的版本
	历史回归测试任务: 成百上千条业务用例如何回归
	总结：加班 + 背锅
3、UI 自动化测试需要哪些技术
	App 自动化测试： Appium、Airtest、ATX 等
4、Appium 介绍
	官网： appium.io
	跨语言 Java、Python、nodejs 等
	跨平台
	Andoid、iOS
	Windows、Mac
	底层多引擎可切换
	生态丰富，社区强大
5、Appium 知识点梳理
    appium测试框架入门
	    appium安装
		appium用例录制
		appium元素定位
		appium等待方式
		appium desirecapbility基本用法
		appium app控件交互
		appium触屏操作
6、企业微信APP项目实战--环境准备
	MacOS 系统
	Android 模拟器（网易 mumu）
	Appium Server、Appium Client
7、企业微信实战（添加成员功能）
	前提条件：
		1、提前注册企业微信管理员帐号
		2、手机端安装企业微信
		3、企业微信 app 处于登录状态
	通讯录添加成员用例步骤
		打开【企业微信】应用
		进入【通讯录】页面
		点击【添加成员】
		点击【手动输入添加】
		输入【姓名】【手机号】并点击【保存】
		验证点：登录成功提示信息
8、总结
	pytest 用法(setup/teardown等)
	DesireCapbility的配置
	元素定位（id，xpath等）
	交互：click(),send_keys()
	特殊元素定位：toast 元素 使用xpath
	等待方式：隐式等待，显式等待
	获取页面源码：driver.get_pagesource
	获取元素的属性：get_attribute
9、企业微信实战（打卡功能）
	前提条件：
		1、提前注册企业微信管理员帐号
		2、手机端安装企业微信
		3、企业微信 app 处于登录状态
	实现打卡功能
		打开【企业微信】应用
		进入【工作台】页面
		点击【打卡】
		选择【外出打卡】tab
		点击【第 N 次打卡】
		验证点：提示【外出打卡成功】
10、总结
	DesireCapbility 跳过设备初始化
	DesireCapbility 动态设置
	swipe 封装滑动操作
	显式等待
11、参考代码 - DesireCapability 配置
	caps["noReset"] = "true"
	caps['settings[waitForIdleTimeout]'] = 0   # 等待页面空闲的时间
	caps['skipServerInstallation'] = ‘true'  # 跳过 uiautomator2 server的安装
	caps['skipDeviceInitialization'] = ‘true'    # 跳过设备初始化
	caps['dontStopAppOnReset'] = ‘true'    # 启动之前不停止app
12、参考代码 - 滚动查找元素
	self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,\
        'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
        .scrollIntoView(new UiSelector().text("添加成员").instance(0));')
13、课后练习
	使用 Appium 实现删除联系人
14、目录
	企业微信实战一（删除联系人）
	打造测试框架的需求与价值
	PO 六大原则
	企业微信实战二（PO 封装）
	框架改进方案
15、企业微信实战（删除成员功能）
	前提条件：
		1、提前注册企业微信管理员帐号
		2、手机端安装企业微信
		3、企业微信 app 处于登录状态
	通讯录添加成员用例步骤
		打开【企业微信】应用
		进入【通讯录】页面
		点击右上角搜索图标，进入搜索页面
		输入搜索内容（已添加的联系人姓名）
		点击展示的第一个联系人（有可能多个），进入联系人详情页面
		点击右上角三个点，进入个人信息页面
		点击【编辑成员】进入编辑成员页面
		点击【删除成员】并确定
	验证点：搜索结果页面联系人个数少一个
16、思路
	输入搜索词
	等待x秒，判断是否有结果
	情况一：【无搜索结果】直接设为 xfail
	情况二：有搜索结果
17、打造测试框架的需求与价值
	1、领域模型适配：封装业务实现，实现业务管理
	2、提高效率：降低用例维护成本，提高执行效率
	3、增强功能：解决已有框架不满足的情况
18、企业微信实战（PO练习）
	企业微信 添加联系人 转为
	企业微信 添加多个联系人 练习
19、测试框架改进
	BasePage 的封装
	初始化方法
	find/finds 方法
	find_and_click 方法
	加入日志
	handle_exception 方法
20、课后作业
	实现添加联系人功能的 PO 封装
	实现删除联系人功能的 PO 封装