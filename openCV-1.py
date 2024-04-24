import cv2

cam = cv2.VideoCapture(0)              # defining a camera  # '0' denotes the position of the webcam

while True:                          # running an infinite loop until we press 'q'
    ignore, frame = cam.read()            # this gives out 2 variables, we only need the second one
  
    greyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cv2.imshow('my WebCam',greyFrame)       # here we diplay the frame that we got from the webcam
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release() 