#https://qiita.com/shoku-pan/items/328edcde833307b164f4
import cv2
#from google.colab.patches import cv2_imshow
img = cv2.imread("/home/shelfer/Desktop/KO/foo-otsu.png")
cv2_imshow(img)
img_gray = cv2.imread("/home/shelfer/Desktop/KO/foo-otsu.png",0)
cv2_imshow(img_gray)
img_sobel = cv2.Sobel(img_gray, cv2.CV_32F, 1, 0, ksize=3)
cv2_imshow(img_sobel)