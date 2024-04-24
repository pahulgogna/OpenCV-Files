import cv2

width = 640
height = 360

snipH = 200
snipW = 200

deltaH = 4
deltaW = 4

BoxCR = int(height/2)
BoxCC = int(width/2)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))



while True:

    ignore, frame = cam.read()

    frameROI = frame[int(BoxCR-snipH/2):int(BoxCR+snipH/2),int(BoxCC - snipW/2):int(BoxCC + snipW/2)]

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)

    if BoxCR-snipH/2 <= 0 or BoxCR+snipH/2 >= height+115:
        deltaH *= (-1)

    if BoxCC - snipW/2 <= 0 or BoxCC + snipW/2 >= width:
        deltaW *= (-1)

    BoxCC += deltaW
    BoxCR += deltaH

    frame[int(BoxCR-snipH/2):int(BoxCR+snipH/2),int(BoxCC - snipW/2):int(BoxCC + snipW/2)] = frameROI

    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)


    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()