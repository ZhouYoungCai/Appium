"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

import logging
# 安装 pyyaml
import yaml


# 读取yaml文件
def get_data(filename):
    logging.info("获取数据")
    with open(filename) as f:
        datas = yaml.safe_load(f)
        return datas
