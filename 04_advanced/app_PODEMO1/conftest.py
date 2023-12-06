"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os
import time
import pytest


# pytest 可以直接获取 rootdir 路径
def get_rootdir(request):
    # 根目录
    rootdir = request.config.rootdir
    return rootdir


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d%H-%M-%S")
    log_name = 'logs/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(os.path.join(get_rootdir(request), log_name))
