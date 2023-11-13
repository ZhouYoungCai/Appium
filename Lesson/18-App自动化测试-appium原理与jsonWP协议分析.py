1、Appium原理与JsonWP协议分析
    理解客户端、appium server、uiautomator2-server的协议
2、Webdriver协议基础知识
	Mobile Json Wire Protocol
	官网：https://github.com/SeleniumHQ/mobile-spec/blob/master/spec-draft.md
	添加的移动端支持的协议：
3、session_id创建
	curl -l-H "Content-type: application /json"-X POST -d '{"desiredCapabilities":
	{ "platformName": "Android" ,"deviceName": "192.168.56.101:5555","platformVersion":"6.0" ,"appPackage": 
	"com.xueqiu.android","appActivity":"com.xueqiu.android.common.MainActivity"l}' 'http://127.0.0.1:4723/wd/hub/session
4、session_id获取
	session_id=$(curl 'http://127.0.0.1:4723/wd/hub/sessions' \ l awk -F\"'{print $6}')
5、element_id获取
	curl -X POST http://127.0.0.1:4723/wd/hub/session/$session_id/elements --data-binary'
	{"using":"xpath", "value":" //*[@text=\ "同意\"]"}' -H "Content-Type: application/json;charset=UTF-8"
6、元素属性获取
	curl http://127.0.0.1:4723/wd/hub/session/$session_id/element/$element_id/ attribute/text
7、元素动作(例如:点击)
	curl -X POST http://127.0.0.1:4723/wd/hub/session/$session_id/element /$element_id/click
8、W3C Webdriver spec
	官网：https://w3c.github.io/webdriver/
	W3C：万维网联盟，国际性中立组织，专门负责统一web相关的标准
	路由信息：

