"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

import pytest


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_name = 'log/' + now + '.logs'
    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)
