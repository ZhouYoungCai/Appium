1、模拟器控制
	只适用Android且为sdk自带的模拟器
	查看sdk模拟器：emulator -list-avds
	设置desired_capability：desired_caps['avd'] = '模拟器名字'
2、capability高级用法
	官网：https://appium.io/
	newCommandTimeout：appium两次请求的间隔时间，默认为60s
	udid：设备唯一标识
	autoGrandPermissions：自动点掉权限弹框，默认为false。注：如果参数noReset为true的话，此capability不起作用。
3、测试策略相关：
	noReset：不对app进行重置操作。针对Android系统，是指不停止app、不清除app数据、不卸载apk
	fullReset：在session开始之前测试结束之后都会，清除app数据并且卸载apk。设置这个参数之前需要设置resetOnSessionStartOnly: true
	如果不设置noReset和fullReset就是默认设置：测试结束后停止app并清除app数据，但是不卸载apk
	dontStopAppOnReset：在重置app时不停止app，相当于复用app，不停止app进程。当设置为true时，
	底层使用的是adb shell am start appPackage/appActivity；当设置为false时会加上 -S 
	参数 adb shell am start -S appPackage/appActivity，会关闭app再重新启动app。
4、性能相关：
	skipServerInstallation：跳过server安装
	skipDeviceInitialization：跳过设备初始化
	skipUnlock：跳过解锁
	skipLogcatCapture：跳过日志获取
	systemPort：获取系统端口号
	ignoreUnimportantViews：跳过不重要组件的获取
	relaxed-security启动的时候设置

