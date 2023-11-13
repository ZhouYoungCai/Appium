1、环境准备
    硬件环境：MAC系统电脑、iOS系统手机或模拟器
    软件环境：Xcode、依赖工具（libimobiledevice、wda、ideviceinstaller等）、被测应用
2、Xcode安装
    官方下载或者APP store下载安装
3、依赖工具
    libimobiledevice  跨平台的协议库和工具，用来支持iPhone等苹果设备的协议
	ideviceinstaller  命令行工具，用于管理IOS设备上应用程序的安装、卸载、升级等，也可以查看app相关的信息
    carthage          是一个IOS项目依赖工具，可以很方便的管理三方依赖，WDA使用这个工具管理项目依赖
    ios-deploy        终端安装和调试iPhone应用的第三方开源库
	ios-webkit-debug-proxy  通过websocket连接代理来自usbmuxd守护进程的请求
	    允许开发人员在真实和模拟的IOS设备上向mobile safari和UIwebviews发送命令
		appium依赖次工具进行webview控件的操作