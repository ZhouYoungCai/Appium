1、内容大纲
    Android/IOS基础知识
	dom结构解读
	id、aid、xpath定位方法
	uiautomatorviewer定位工具使用
2、Android基础知识
    Android是通过容器的布局属性来管理子控件的位置关系，布局过程就是把界面上的所有的控件，
	    根据它们的间距的大小，摆放在正确位置
	Android七大布局：
	    LinearLayout(线性布局)----水平和垂直
		RelativeLayout（相对布局）
		FrameLayout（帧布局）
		AbsoluteLayout（绝对布局）
		TableLayout（表格布局）
		GridLayout（网格布局）
		ConstraintLayout（约束布局）
3、Android四大组件
    activity            与用户交互的可视化界面
	service             实现程序后台运行的解决方案
	content provider    内容提供者，提供程序所需要的数据
	broadcast receiver  广播接收器，监听外部事件的到来（比如来电）
4、常用的控件
    textview（文本控件），edittext（可编辑文本控件）
	button（按钮），imagebutton（图片按钮），togglebutton（开关按钮）
	imageview（图片控件）
	checkbox（复选框控件）、radiobutton（单选框控件）
5、布局 
    布局是一种可用于放置很多控件的容器，它可以按照一定的规律调整内部控件的位置，
	从而编写出精美的页面。当然，布局的内部出了放置控件外，也可以放置布局，
	通过多层布局的嵌套，我们就能够完成一些比较复杂的界面。
6、IOS基础知识
    iOS介绍：
	    由苹果公司为iPhone开发的操作系统，主要给iPhone、itouch、iPad使用
		原名为iPhoneOS，2010年WWDC大会改名为IOS
		目前IOS最新版本是IOS15.6.1
	布局：
	    IOS去掉了布局的概念，直接用变量之间的相对关系完成位置的计算
	开发环境：
	    系统：macOSX
		开发工具：xcode
		开发语言：ObjectC
		安装文件：.ipa文件/.app文件
	注意：
	    使用appium测试IOS应用需要使用MacOS操作系统
7、元素定位
    元素定位，实际上就是定位控件
	要想一个脚本同时支持Android/IOS两个系统，就得保证元素属性（id、aid、xpath等）一致
8、控件基础知识
    dom：document object model 文档对象模型
	dom应用：最早应用于html和js的交互。用于表示界面的控件层级，界面的结构化描述，常见的格式为html、xml。
	         核心元素为节点和属性
	xpath：xml路径语言，用于xml中的节点定位
9、定位方法
    测试步骤三要素：定位、交互、断言
	定位方式：
	    id定位：
		    driver.find_element_by_id(resource-id属性值)
			driver.find_element(MobileBy.ID,"resource:id")
		accessibility_id定位：
		    driver.find_element_by_accessibility_id(content-desc属性值)
			driver.find_element(MobileBy.ACCESSIBILITY_ID,"content_desc:属性")
		xpath定位：
		    driver,find_element_by_xpath(xpath属性值)
		classname定位（不推荐）
10、定位工具 
    uiautomatorviewer工具（only android）
	推荐使用
	sdk路径下的工具
	appium inspector工具