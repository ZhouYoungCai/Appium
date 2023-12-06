"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from time import sleep

import easyocr
import requests
import cv2


class OCRCode:

    @classmethod
    def get_by_ocr(cls, img_url):
        # 使用requests发请求拿到图片结果
        result = requests.get(img_url, verify=False)
        # 保存图片到本地
        with open("code.png", "wb") as f:
            f.write(result.content)
        sleep(1)
        # opencv处理图片
        cls.opencv_image()
        # 实例化easyocr
        ocr = easyocr.Reader(['ch_sim', 'en'])
        # 识别图片内容
        code = ocr.readtext("result.png")[0][1].replace(" ", "")
        print(code)
        return code

    @classmethod
    def opencv_image(cls):
        # 读取图片
        image = cv2.imread("code.png")
        # 边缘保留滤波去噪
        image1 = cv2.pyrMeanShiftFiltering(image, sp=8, sr=60)
        # 灰度图片，颜色处理
        image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        # 颜色取反
        cv2.bitwise_not(image2, image2)
        # 保存图片
        cv2.imwrite("result.png", image2)