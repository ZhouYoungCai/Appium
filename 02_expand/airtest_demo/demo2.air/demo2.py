# -*- encoding=utf8 -*-
__author__ = "juanxu"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
poco(text="企业微信").click()
poco(selected="True").click()
poco("com.tencent.wework:id/jqr").offspring("com.tencent.wework:id/dyx").offspring("com.tencent.wework:id/c1a").child(
    "com.tencent.wework:id/fzk")[5].offspring("com.tencent.wework:id/kvu").click()
poco(text="手动输入添加").click()
poco("com.tencent.wework:id/bsm").set_text('aaaaaa')
poco("com.tencent.wework:id/hgi").set_text('13100000000')
poco("com.tencent.wework:id/at6").click()
