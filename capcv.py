#https://konchangakita.hatenablog.com/entry/2020/07/27/220000
import cv2 as cv
# ESCキーを押すと終了します
#カメラインスタンス作成
cap = cv.VideoCapture(0)

assert cap.isOpened(), 'Cannot capture source'

try:   
    while True:
        ret, frame = cap.read()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break

        cv.imshow('OpenCV - test', frame)
        
        if cv.waitKey(10) == 27:
            break

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    print("\nCamera Interrupt")

finally:
    cap.release()
    cv.destroyAllWindows()