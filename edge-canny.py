#https://shikaku-mafia.com/opencv-edge/
import cv2


img = cv2.imread('./foo.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_after = cv2.Canny(img_gray, 100, 112)

cv2.imwrite('./foo_after.png', img_after)