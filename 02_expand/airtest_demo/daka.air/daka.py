# -*- encoding=utf8 -*-
__author__ = "juanxu"

from airtest.core.api import *

# auto_setup(__file__)
# connect_device('Android:///emulator-5554')


touch(Template(r"tpl1655199009169.png", record_pos=(0.001, -0.221), resolution=(936, 1664)))
touch(Template(r"tpl1655199019195.png", record_pos=(0.208, 0.81), resolution=(936, 1664)))
swipe(Template(r"tpl1655199074155.png", record_pos=(0.004, 0.554), resolution=(936, 1664)), vector=[0.0053, -0.6005])
touch(wait(Template(r"tpl1655199092564.png", record_pos=(-0.316, 0.316), resolution=(936, 1664))))
sleep(3.0)

wait(Template(r"tpl1655201517359.png", record_pos=(-0.243, -0.641), resolution=(936, 1664)))

touch(Template(r"tpl1655201541529.png", record_pos=(0.264, -0.625), resolution=(936, 1664)))

wait(Template(r"tpl1655201569579.png", record_pos=(0.017, -0.109), resolution=(936, 1664)))

touch((464, 1080))

snapshot(msg="打卡完成.")

assert_exists(Template(r"tpl1655199218052.png", record_pos=(0.024, -0.007), resolution=(936, 1664)), "请填写测试点")

keyevent("4")
keyevent("4")
