#https://pystyle.info/opencv-otsu-method/
import cv2
import numpy as np
from IPython.display import display, Image

def imshow(img):
    """ndarray 配列をインラインで Notebook 上に表示する。
    """
    ret, encoded = cv2.imencode("foo.png", img)
    display(Image(encoded))


# 画像を読み込む。
img = cv2.imread("foo.png")

# グレースケール形式に変換する。
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 大津の手法
ret, bin_img = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
print(f"threshold: {ret}")
imshow(bin_img)