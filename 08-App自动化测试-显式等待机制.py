1、等待方式
    强制等待：sleep，不推荐
	全局隐式等待：在服务端等待，driver.implicitly_wait(timeout)
	显式等待:在客户端等待，webdriverwait(self.driver,10).until(expected_conditions.visibility_of_element_located(LOCATOR))
2、显示等待
    显示等待与隐式等待相对，显示等待必须在每个需要等待的元素前面进行声明。
	是针对某个特定的元素设置的等待时间，在设置时间内，默认每隔一段时间检测一次当前页面某个元素是否存在。
	如果在规定时间内找到了元素，则直接执行，即找到了元素就执行相关操作
	如果超过设置时间检测不到则抛出异常。默认检测频率为0.5s，默认抛出异常为：NoSuchElementException
	显示等待用到的两个类：
	    WebDriverWait和expected_conditions两个类
3、显示等待 
    显示等待可以等待动态加载的ajax元素，显示等待需要使expectedconditions来检查条件
	一般页面上元素的呈现
	    title出现  首先出现title
		dom树出现  presence，还不完整
		css出现   （可见visibility）
		js出现，js特效执行（可点击clickable）
	html文档是自上而下加载的
	js文件加载会阻塞HTml内容的加载，有些JS异步加载的方式来完成JS的加载
	样式表下载完成之后会跟前面的样式表一起进行解析，会对之前的元素重新渲染
4、webdriver用法
    WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_expections=None)
5、使用lambda表达式
    webdriverwait(driver,time)untile(lambda x:x.find_element_by_id("someid"))返回一个元素