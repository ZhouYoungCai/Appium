# -*- encoding=utf8 -*-
__author__ = "juanxu"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1655188163943.png", record_pos=(0.001, -0.222), resolution=(936, 1664)))

touch(wait(Template(r"tpl1655188269757.png", record_pos=(0.405, 0.81), resolution=(936, 1664))))

touch(Template(r"tpl1655188479090.png", record_pos=(-0.234, 0.122), resolution=(936, 1664)))
touch(Template(r"tpl1655188488438.png", record_pos=(-0.158, 0.162), resolution=(936, 1664)))

touch(Template(r"tpl1655189708049.png", record_pos=(-0.082, -0.605), resolution=(936, 1664)))

text("hogwarts")
touch(Template(r"tpl1655188575023.png", record_pos=(0.139, -0.459), resolution=(936, 1664)))

text("13100000033")
touch(Template(r"tpl1655188593811.png", record_pos=(-0.248, -0.225), resolution=(936, 1664)))

# sleep(5.0)
# assert_exists(Template(r"tpl1655190806939.png", record_pos=(-0.238, -0.761), resolution=(936, 1664)), "判断返回")

print(str(poco(text="添加成功").attr("text")))

# assert_equal(str(poco(text="添加成功").attr("text")), "添加成功", "toast 弹框文字")
