import cv2
import numpy as np

def myCallback1(val):
    global hueLow
    hueLow = val
def myCallback2(val):
    global hueHigh
    hueHigh = val
def myCallback3(val):
    global satLow
    satLow = val
def myCallback4(val):
    global satHigh
    satHigh = val
def myCallback5(val):
    global valLow
    valLow = val
def myCallback6(val):
    global valHigh
    valHigh = val
hueHigh = 20
hueLow = 10
satLow = 10
satHigh = 250
valLow = 10
valHigh = 250

width = 640
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('tracker')
cv2.resizeWindow('tracker', 500, 300)
cv2.moveWindow('tracker', width,0)
cv2.createTrackbar('Hue Low','tracker',10,180,myCallback1)
cv2.createTrackbar('Hue High','tracker',10,180,myCallback2)
cv2.createTrackbar('sat Low','tracker',10,255,myCallback3)
cv2.createTrackbar('sat High','tracker',250,255,myCallback4)
cv2.createTrackbar('val Low','tracker',10,255,myCallback5)
cv2.createTrackbar('val High','tracker',10,255,myCallback6)

while True:
    _, frame = cam.read()
    lowerBound = np.array([hueLow,satLow,valLow])
    higherBound = np.array([hueHigh,satHigh,valHigh])
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,lowerBound,higherBound,)
    cv2.imshow('mask',mask)
    cv2.moveWindow('mask',0,height)
    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)


    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()