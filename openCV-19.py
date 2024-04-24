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

width = 640
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

threshold = 400
hueHigh = 40
hueLow = 26
satLow = 110
satHigh = 255
valLow = 120
valHigh = 255

cv2.namedWindow('cam1')
# cv2.namedWindow('tracker')
# cv2.resizeWindow('tracker', 500, 300)
# cv2.moveWindow('tracker', width,0)
# cv2.createTrackbar('Hue Low','tracker',hueLow,180,myCallback1)
# cv2.createTrackbar('Hue High','tracker',hueHigh,180,myCallback2)
# cv2.createTrackbar('sat Low','tracker',satLow,255,myCallback3)
# cv2.createTrackbar('sat High','tracker',satHigh,255,myCallback4)
# cv2.createTrackbar('val Low','tracker',valLow,255,myCallback5)
# cv2.createTrackbar('val High','tracker',valHigh,255,myCallback6)

i = 0

while True:
    _,frame = cam.read()
    lowerRange = np.array([hueLow,satLow,valLow])
    higherRange = np.array([hueHigh,satHigh,valHigh])
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,lowerRange,higherRange)

    contours,noNeed = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > threshold:
            x,y,widthC,heightC = cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y), (x+widthC,y+heightC),(255,255,255),2)
            cv2.moveWindow('cam1',x,y)
 
    cv2.imshow('cam1',frame)
    if i == 0:
        cv2.moveWindow('cam1',0,0)
        i = 1
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.release()