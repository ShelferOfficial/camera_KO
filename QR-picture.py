#https://blog.tkrel.com/12973
import cv2
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
while True:
#cap.release()
#KO while(cap.isOpened()):
ret, frame = cap.read()
img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
height = img.shape[0]
width = img.shape[1]
image = cv2.resize(img , (int(width*0.5), int(height*0.5)))

data = decode(image)
if len(data) > 0:
  # 結果が返ってきた場合
  print(data[0][0].decode('utf-8', 'ignore'))
  break

cap.release()