#https://qiita.com/igor-bond16/items/0dbef691a71c2e5e37d7
from pyzbar.pyzbar import decode
import cv2

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        d = decode(frame)
        if d:
            frame = cv2.putText(frame,d[0].data.decode('utf-8'),(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()