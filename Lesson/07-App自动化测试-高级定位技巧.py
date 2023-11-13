1、Xpath定位进阶
    层级定位：
	    父节点定位子节点
		子节点定位父节点
		子节点定位兄弟节点
		爷爷节点定位孙子节点
2、UI automator定位
    优点：xpath定位速度慢，uiautomator是Android的工作引擎，速度快
	缺点：表达式书写复杂，容易写错IDE没有提示
3、UI automator定位
    通过resource-id定位
	    new UiSelector().resourceId("id")
	通过classname定位
	    new UiSelector().className("className")
	通过content-desc定位
	    new UiSelector().description("content-des属性")
	通过文本定位
	组合定位
	通过父子关系定位