# -*- encoding=utf8 -*-
__author__ = "juanxu"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
connect_device('Android:///emulator-5554')
touch(Template(r"tpl1655454312989.png", record_pos=(-0.001, -0.222), resolution=(936, 1664)))

# 进入 工作台

touch(wait(Template(r"tpl1655454350550.png", record_pos=(0.206, 0.807), resolution=(936, 1664))))

# 滑动操作
swipe(Template(r"tpl1655454416372.png", record_pos=(0.017, 0.393), resolution=(936, 1664)), vector=[-0.0203, -0.6689],
      duration=2)

# 点击打卡
touch(wait(Template(r"tpl1655454454247.png", record_pos=(-0.316, 0.319), resolution=(936, 1664))))

wait(Template(r"tpl1655454548163.png", record_pos=(-0.298, -0.757), resolution=(936, 1664)))

# 点击外出打卡

touch(Template(r"tpl1655454525364.png", record_pos=(0.261, -0.65), resolution=(936, 1664)))

touch(Template(r"tpl1655454580407.png", record_pos=(0.034, 0.322), resolution=(936, 1664)))

snapshot(msg="打卡点击完成.")

# 判断打卡成功

assert_exists(Template(r"tpl1655454617766.png", record_pos=(0.005, -0.199), resolution=(936, 1664)), "判断打卡成功")
