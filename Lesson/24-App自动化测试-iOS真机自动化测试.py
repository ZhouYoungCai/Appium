1、目录
    连接真机
	安装应用
	配置desired capabilities
	常见问题分析
2、连接真机
    准备一个开发者证书
	使用USB线
	真机需要连接网络（验证证书）
3、安装应用
    方法1：build应用到手机上
	    信任证书:设置--通用--设备管理--信任开发者证书
	方法2：
	    ideviceinstaller--install/-i xx.app
4、问题1
    问题：appium inspector启动session的时候，报错，提示没有对应的模拟器设备
	解决：设置真机desired capability没有设置udid
	


