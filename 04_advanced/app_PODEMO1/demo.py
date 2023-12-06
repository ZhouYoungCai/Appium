"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


def pz_fun():
    print("start")
    fun()
    print("end")


def zs_fun(fun):
    def wrapper(*args, **kwargs):
        print("start")
        fun(*args, **kwargs)
        print("end")

    return wrapper


@zs_fun
def fun(a, b):
    print(f"a={a} b={b}")


# 调用方法1
# fun = zs_fun(fun)
# fun()

# 调用方法2
fun(1, 2)
