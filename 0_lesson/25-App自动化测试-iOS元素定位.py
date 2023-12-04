1、页面结构分析
    启动appium server version：1.22.0
	inspector APP version：2021.12.2
	配置 Desire Capability
2、定位表达式结构
    IOS predicate string 定位表达式结构：属性+运算符+值
3、元素属性
	type: 元素类型，等同于 className
	name: 当前元素的文本信息，一般等于 label
	label: 与 name 一致
	enabled: 当前元素是否可点击,一般为 true 或 false
	visible: 当前元素是否可见,一般为 true 或 false
4、比较运算符
	==，>=，<=，>，<，!=，<>，可用来比较数值或字符串
	例如：
	label == "SYSTEM (TEXT)"
5、逻辑运算符
	AND，OR，NOT，AND等同于&&；OR等同于||；NOT等同于!
	例如：
	label == "SYSTEM (TEXT)" AND enabled == true
6、模糊匹配LIKE
	? 和 * 都可以作为通配符，?匹配一个字符，*匹配多个字符。
	例如：
	label LIKE "SYSTEM (TEXT)"
7、其他
	BEGINSWITH，ENDSWITH，CONTAINS
	例如：
	# 匹配属性为 label ，value为 SYSTEM 开头的元素
