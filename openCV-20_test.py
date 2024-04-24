import cv2
import time

width = 640
height = 480
sensitivity = 2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')  # getting the face detection model into the code by using a reletive path

lastTime = time.time()
time.sleep(1)

while True:
    dt =  time.time() - lastTime
    # lastTime = time.time()
    # fps = 1/dt
    # print(int(fps))
    _, frame = cam.read()
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,sensitivity,5)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)

    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()