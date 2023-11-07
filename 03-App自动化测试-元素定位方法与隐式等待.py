1、测试用例的重要组成部分
    导入依赖：from appium import webdriver
	capabilities设置：初始化driver：python webdriver.remote
	隐式等待，增强用例的稳定性
	元素定位与操作 find+action
	断言 assert
2、capabilities设置
    app apk地址
	app Package包名
	appActivity  Activity名字
	automationName 默认使用uiautomator2(安卓默认使用uiautomator2，IOS默认使用XCUITest)
    noReset fullReset是否在测试前后重置相关环境（例如首次打开弹框，或者是登录信息）
	    演示雪球的首次启动弹框功能，noreset=True，noreset=False情况
	Unicodekyeboard resetkeyboard是否需要输入非英文之外的语言并在测试完成后重置输入法
	    举例输入中文，alibaba，阿里巴巴
	dontstopapponreset首次启动的时候，不停止APP（可以调试或者运行的时候提升运行速度）
	skipdeviceinitialization跳过安装，权限设置等操作（可以调试或者运行的时候提升运行速度）
