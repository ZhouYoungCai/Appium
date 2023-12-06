"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from hamcrest import assert_that, close_to

from app_demo1.app_PODEMO.base.xueqiu_app import XueQiuApp


class TestXueQiu:

    def setup_class(self):
        # 启动app
        self.xueqiuapp = XueQiuApp()

    def setup(self):
        self.main = self.xueqiuapp.start().goto_main()

    def teardown_class(self):
        self.xueqiuapp.stop()

    def test_search1(self):
        """
        打开【雪球】应用首页
        点击搜索框，进入搜索页面
        向搜索输入框中输入【alibaba】
        点击搜索结果中的【阿里巴巴】
        切换到 tab 的【股票】
        找到 股票【阿里巴巴】的股票价格 price
        判断 price 在 110 上下 10%浮动
        :return:
        """
        search_key = "alibaba"
        search_result = 'BABA'
        stock_price = self.main.click_search(). \
            input_searchcontent(search_key). \
            click_searchresult(search_result). \
            goto_stock_tab().get_price()

        # hamcrest 接近某个值的范围
        assert_that(stock_price, close_to(110, 110 * 0.1))

    def test_search2(self):
        """
        打开【雪球】应用首页
        点击搜索框，进入搜索页面
        向搜索输入框中输入【alibaba】
        点击搜索结果中的【阿里巴巴】
        切换到 tab 的【股票】
        找到 股票【阿里巴巴】的股票价格 price
        判断 price 在 110 上下 10%浮动
        :return:
        """
        search_key = "alibaba"
        search_result = 'BABA'
        stock_price = self.main.click_search(). \
            input_searchcontent(search_key). \
            click_searchresult(search_result). \
            goto_stock_tab().get_price()

        # hamcrest 接近某个值的范围
        assert_that(stock_price, close_to(110, 110 * 0.1))
