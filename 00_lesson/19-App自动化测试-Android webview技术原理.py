1、目录
	WebView日志获取
	关键日志分析
	问题分析定位
2、WebView日志获取
	appium -g appium.log | tee来收集日志
	日志中有一条命令：adb shell cat /proc/net/unix，手动执行后的结果如下：
	此时手机端相当于服务端，appium server相当于客户端
	域套接字：Unix中进程与进程之间通讯的一种方式，客户端与服务端要建立通讯至少要建立一个套接字，客户端与服务端建立连接是靠共同的套接字和相应的服务端的端口号。套接字会处于监控状态，来监听客户端发来的请求。
3、获取所有的webview套接字：adb shell cat /proc/net/unix | grep webview
4、获取webview进程：adb shell ps | grep [进程号]
5、启动chromedriver：Spawning chromedriver with: /Documents/mychromedriver/all/chromedriver2_20 --url-base=wd/hub --port=8.0--adb-port=5037 --verbose
	转发请求，将appium server 的请求转发给chromedriver
	Proxying [POST/wd/hub/session/11f8C2c1-2752-4b4b-afae-eec11eebc0c4/element] to [POST http://127.0.0.1:800/wd/hub/ session/4ca23383b719f48e63c169894803121f/element] with body: {"using" :"xpath", "value" "//*[ id=Layout_app_3V4I"]/div/div/u1/li[1]/div[2]/h1"}
6、问题分析定位
