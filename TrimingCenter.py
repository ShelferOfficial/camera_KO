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