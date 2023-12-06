1、常用命令
    查看设备
	启动模拟器
	安装应用
    卸载应用
	查看应用bundle ID
2、操作模拟器命令：xcrun simctl
    操作真机命令：idevice<xxx>
3、查看设备
    查看模拟器列表
	查看真机设备列表
	xcrun simctl list device  #查看已安装的模拟器
	xcrun simctl list device | grep Booted  #查看已经开机的模拟器
	idevice_id -l  #查看已经连接的真机设备的udid信息
4、启动模拟器
    启动模拟器命令：xcrun simctl boot <device>
    查看模拟器列表：xcrun simctl list devices
	启动模拟器：xcrun simctl boot 模拟器ID
5、安装应用
    模拟器安装应用
	单设备：xcrun simctl install booted demo.app
	多设备：xcrun simctl install <device> demo.app
	真机安装应用
	ideviceinstaller --install </path/to/file/xxx.app>
	ideviceinstaller -i </path/to/file/xxx.app>
6、卸载应用
    模拟器卸载应用
	xcrun simctl unistall <device> <bundleID>
	真机卸载应用
	ideviceinstaller --uninstall <appid>
	ideviceinstall -U <appid>
7、查看应用的bundleID
    模拟器查看应用bundleID
	    找到app的安装包
		右键点击
		显示包内容
		找到info.plist文件
		双击打开，就可以找到对应的bundle identifier项
	真机查看应用的bundleid
	    ideviceinstaller -l
8、总结
    模拟器使用xcrun simctl命令来操作，比如启动模拟器，安装应用，卸载应用等
	真机使用idevice_xxx来操作
	可以通过命令来完成很多事情，比如查看设备、启动模拟器、安装应用、鞋子应用、
	截图命令、查看应用bundleID等。