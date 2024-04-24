import cv2
import time

width = 640
height = 360


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

lastTime = time.time()
time.sleep(.1)

while True:

    dt = time.time() - lastTime
    lastTime = time.time()
    fps = 1/dt

    _, frame = cam.read()

    cv2.putText(frame, f'fps = {int(fps)}',(int(height/10),int(width/10)),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
    cv2.imshow('my Cam',frame)



    if cv2.waitKey(1)== ord('q'):
        break


cv2.release()