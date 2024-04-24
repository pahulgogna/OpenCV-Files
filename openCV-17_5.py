import cv2
import numpy as np

def MouseCallback(event, xPos, yPos, flags, params):
    
    global evt    
    global position
    if event == cv2.EVENT_LBUTTONDOWN:
        position = (xPos,yPos)
        evt = event
evt =0
hueHigh = 20
hueLow = 10
satLow = 10
satHigh = 250
valLow = 10
valHigh = 250

hueRange = 20
satRange = 50
valRange = 60

width = 640
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('screen1')
cv2.setMouseCallback('screen1',MouseCallback)

while True:
    _, frame = cam.read()

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if evt == 1:
        HSVcolor = frameHSV[position[1],position[0]]
        print(HSVcolor)
        hueHigh = HSVcolor[0] + hueRange
        hueLow = HSVcolor[0] - hueRange
        satLow = HSVcolor[1] - satRange
        satHigh = HSVcolor[1] + satRange
        valLow = HSVcolor[2] - valRange
        valHigh = HSVcolor[2] + valRange
        evt = 0
    lowerBound = np.array([hueLow,satLow,valLow])
    higherBound = np.array([hueHigh,satHigh,valHigh])

    mask = cv2.inRange(frameHSV,lowerBound,higherBound,)
    cv2.imshow('mask',mask)
    cv2.moveWindow('mask',width + 20,0)
    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)


    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()