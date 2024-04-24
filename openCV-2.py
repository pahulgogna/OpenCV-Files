import cv2

width = 640
height = 480

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    _, frame = cam.read()

    # Screen1 # Top left
    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)


    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()