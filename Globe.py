#https://iotdiyclub.net/raspberry-pi-camera-python-1/
import time
import picamera
 
with picamera.PiCamera() as camera:
 camera.resolution = (1024, 768)
 camera.start_preview()
 # Camera warm-up time
 time.sleep(5)
 camera.capture('foo.png')
 

#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 入力画像の読み込み
img = cv2.imread("/home/shelfer/Desktop/KO/foo.png")

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 方法2 （OpenCVで実装）
ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

# 結果を出力
cv2.imwrite("/home/shelfer/Desktop/KO/foo-otsu.png", th)

#https://maywork.net/computer/python-trim-center/
#!/usr/bin/env python3
# coding: utf8

import cv2
import numpy as np
import os, glob


# 画像を中心から指定サイズで切り出し

def trim_center(img, width, height):
    h, w = img.shape[:2]
    
    top = int((h / 2) - (height / 1.2))
    bottom = top+height
    left = int((w / 2) - (width / 2))
    right = left+width
    
    return img[top:bottom, left:right]

if __name__ == '__main__':
    src_file = '/home/shelfer/Desktop/KO/foo-otsu.png'
    width = height = 300
    img = cv2.imread(src_file)
    dst = trim_center(img, width, height)
    cv2.imwrite('foo-triCenter.png', dst)
    
#https://motojapan.hateblo.jp/entry/2018/03/12/094636
import time
import pyocr
from PIL import Image
import pyocr.builders

#img : PIL image
img=Image.open('/home/shelfer/Desktop/KO/foo-triCenter.png')
def get_digit_ocr_info(img):
    result = None
    start_time = time.time()
    #print('******** start convert_image_to_deadline  *********')

    width, height=img.size

    tools = pyocr.get_available_tools()
    tool = tools[0]
    #print(tool)
    langs = tool.get_available_languages()
    #print("support langs: %s" % ", ".join(langs))
    #lang = langs[0]
    lang = 'eng'  #言語設定で、「英語」を選択

    digit_txt = tool.image_to_string(
      img,
      lang=lang,
      builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    #print('TextBuilder', digit_txt)
    print(digit_txt)

    #print('******** end convert_image_to_deadline  *********')
    return digit_txt
get_digit_ocr_info(img)