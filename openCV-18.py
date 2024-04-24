import cv2
import numpy as np
import time

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

threshold = 600
hueHigh =150
hueLow = 80
satLow = 110
satHigh = 255
valLow = 120
valHigh = 255

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
cv2.createTrackbar('Hue Low','tracker',80,180,myCallback1)
cv2.createTrackbar('Hue High','tracker',150,180,myCallback2)
cv2.createTrackbar('sat Low','tracker',110,255,myCallback3)
cv2.createTrackbar('sat High','tracker',255,255,myCallback4)
cv2.createTrackbar('val Low','tracker',120,255,myCallback5)
cv2.createTrackbar('val High','tracker',255,255,myCallback6)

lastTime = time.time()
time.sleep(.1)

while True:

    dt = time.time() - lastTime
    lastTime = time.time()
    fps = 1/dt
    print(fps)

    _, frame = cam.read()
    lowerBound = np.array([hueLow,satLow,valLow])
    higherBound = np.array([hueHigh,satHigh,valHigh])
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,lowerBound,higherBound,)

    contours,noNeed = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)  # Finding contours in mask
    for contour in contours:  # iterating through the array of contours (contour itself is an array of x,y positions)
        area = cv2.contourArea(contour)

        if area > threshold:

            x,y,widthC,heightC = cv2.boundingRect(contour)

            cv2.rectangle(frame,(x,y),(x+widthC,y+heightC),(255,255,255),3)

    cv2.imshow('mask',mask)  # to show the mask created (used for tuning the selection)
    cv2.moveWindow('mask',100,height)
    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)


    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()