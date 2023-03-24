#https://qiita.com/ikanamazu/items/d752225a0a9834ce0d41

import cv2
img = cv2.imread("foo-otsu.png")
img1 = img[550 : 1800, 1000: 2000]
cv2.imwrite("foo-otsu-tri.png",img1)