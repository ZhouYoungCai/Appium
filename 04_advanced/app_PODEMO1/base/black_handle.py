"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging
import os.path
import time
import traceback
from time import sleep

# def black_wrapper(fun):
#     def run(*args,**kwargs):
#         print(f"args ====>{args}")
#         basepage = args[0]
#
#         try:
#             return fun(*args,**kwargs)
#         except Exception as e:
#             for black in basepage.black_list:
#                 eles = basepage.driver.find_elements(*black)
#                 if len(eles) >0:
#                     eles[0].click()
#                     return basepage.find(*args,**kwargs)
#             raise e
#     return run

# 声明一个黑名单
import allure
from appium.webdriver.common.appiumby import AppiumBy


# black_list = [(AppiumBy.ID, "com.xueqiu.android:id/iv_close")]

# 注意这里的fun 就是代表 find ，要把里面的find都改为fun


def black_wrapper(fun):
    def run(*args, **kwargs):
        from app_demo1.app_PODEMO1.base.base_page import BasePage
        basepage: BasePage = args[0]
        try:
            logging.info(f"开始查找元素：{args[2]}")
            return fun(*args, **kwargs)
        except Exception as e:
            logging.warning("未找到元素，处理导演 ")
            # 以当前时间命名的 截图
            curtime = basepage.get_time()
            tmp_name = curtime + ".png"
            # 当前black_handle.py所在的路径
            logging.info("当前保存图片的路径 >>>" + os.path.dirname(__file__))
            # 找到images 路径 ，拼接图片名称
            tmp_path = os.path.join(os.path.dirname(__file__), "..", "images", tmp_name)
            basepage.screenshot(tmp_path)
            allure.attach.file(tmp_path, name="查找截图", attachment_type=allure.attachment_type.PNG)
            for black in basepage.black_list:
                logging.info(f"处理黑名单：{black}")
                eles = basepage.driver.find_elements(*black)
                if len(eles) > 0:
                    logging.info(f"点击黑名单弹框")
                    eles[0].click()
                    return fun(*args, **kwargs)
            logging.error(f"遍历黑名单，仍未找到元素，异常信息 ====> {e}")
            logging.error(f"traceback.format_exc() ====> {traceback.format_exc()}")
            raise e

    return run
