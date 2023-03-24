#https://iotdiyclub.net/raspberry-pi-camera-python-1/
import time
import picamera
 
with picamera.PiCamera() as camera:
 camera.resolution = (1024, 768)
 camera.start_preview()
 # Camera warm-up time
 time.sleep(5)
 camera.capture('foo.png')