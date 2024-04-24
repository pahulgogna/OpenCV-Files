import cv2 
import numpy as np

MyCam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

width = 620
height = 360

MyCam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
MyCam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
MyCam.set(cv2.CAP_PROP_FPS, 30)
MyCam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Cam 1')

evt = 0

def MouseClick(event,xPos,yPos,flags, params):

    global evt 
    global x
    global y

    if event == cv2.EVENT_LBUTTONDOWN:
        print('event = ',event, ', xPos = ',xPos,', yPos = ',yPos)
        evt = event
        x,y = xPos, yPos
    if event == cv2.EVENT_LBUTTONUP:
        print('event = ',event, ', xPos = ',xPos,', yPos = ',yPos)
        evt = event
        x,y = xPos, yPos

    if event == cv2.EVENT_RBUTTONDOWN:
        evt = event

cv2.namedWindow('Cam 1')
cv2.setMouseCallback('Cam 1', MouseClick)

while True:

    _,frame = MyCam.read()

   

    if evt == 1 or evt == 4:
        cv2.circle(frame, (x,y),20,(0,255,0),2)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    cv2.imshow('Cam 1', frame)

MyCam.release()