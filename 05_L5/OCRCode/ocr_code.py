"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from time import sleep

import easyocr
import requests


class OcrCode:

    @classmethod
    def get_by_ocr(cls, img_url):
        # 使用requests 发请求拿到图片结果
        result = requests.get(img_url, verify=False)
        # 保存图片到本地
        with open("code.png", "wb") as f:
            f.write(result.content)
        sleep(1)
        # 实例化easyocr
        ocr = easyocr.Reader(['ch_sim', 'en'])
        # 识别图片内容，并去掉空格
        code = ocr.readtext("code.png")[0][1].replace(" ", "")
        print(f"识别到的验证码为: {code}")
        return code