import cv2
import time

width = 640
height = 480
sensitivity = 1.3
sensitivityE = 1.1

white = (255,255,255)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')  # getting the face detection model into the code by using a reletive path
eyesCascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')

lastTime = time.time()
time.sleep(1)

while True:
    dt =  time.time() - lastTime
    lastTime = time.time()
    fps = 1/dt
    print(int(fps))
    _, frame = cam.read()
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(frameGray,sensitivity,5)
    for face in faces:
        xROI,yROI,w,h = face
        cv2.rectangle(frame,(xROI,yROI,xROI+w,yROI+h),white,2)
        frameROI = frameGray[yROI:(yROI+h),xROI:(xROI+w)]
        # cv2.imshow('frameROI',frameROI)
        # cv2.moveWindow('frameROI',width,0)
        eyes = eyesCascade.detectMultiScale(frameROI)
        for eye in eyes:
            x,y,w,h = eye 
            cv2.rectangle(frame,(xROI+x,yROI + y),((xROI+x+w),(yROI+y+h)),white,3)


    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)

    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()