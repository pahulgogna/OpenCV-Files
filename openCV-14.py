import cv2
import numpy as np

print(cv2.__version__)

evt = 0
ColorFrame = np.zeros((250,250,3),dtype=np.uint8)

def MouseCallback(event,xPos,yPos,flags,params):
    global evt 
    global pos
    global color_tuple
    evt = event
    if evt == cv2.EVENT_LBUTTONDOWN:
        pos = (xPos,yPos)
        color_tuple = frame[pos[1],pos[0]]
        # print(color_tuple)
        cv2.imshow('colored', ColorFrame)
        cv2.moveWindow('colored', width,0)

width=680
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam',MouseCallback)

while True:
    ignore,  frame = cam.read()

    if evt == 1:
        ColorFrame[:,:] = color_tuple
    cv2.imshow('colored', ColorFrame)
    cv2.moveWindow('colored', width,0)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()