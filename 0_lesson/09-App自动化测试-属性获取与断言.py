1、断言
    普通断言assert
	举例：
		def test_assert(self):
			a = 10
			b = 20
			assert a < b
			assert 'h' in 'this'
	Hamcrest断言
2、Hamcrest断言
    GitHub地址：https://github.com/hamcrest/PyHamcrest
	hamcrest框架介绍
	    hamcreast是一个为了测试为目的，能组合成灵活表达式的匹配器类库。
		用于编写断言的框架，使用这个框架编写断言，提高可读性及开发测试的效率。
	    hamcrest提供了大量被称为“匹配器”的方。每个匹配器都设计用于执行特定的比较操作。
		hamcrest的可拓展性强，让你能够创建自定义的匹配器。
		支持多种语言，Java，python，ruby，objective-C，php，erlang，swift
