import cv2
import mediapipe as mp
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

width = 1280
height = 720

cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)

hands = mp.solutions.hands.Hands(False,2,1,.5,.5)
myDraw = mp.solutions.drawing_utils

while True:
    _,frame = cam.read()
    cv2.flip(frame,1)
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:  # here we itterate through an array of arrays of different hands
            MyHand = []
            for landmarks in handLandmarks.landmark:  # here we itterate through the landmarks of the current hand
                # print(f'(x = {landmarks.x}, y = {landmarks.y}, z = {landmarks.z})')
                MyHand.append((int(width*landmarks.x),int(height*landmarks.y)))
                # print(MyHand)
            centre = MyHand[20]  # 20 is the index for the tip of the pinky finger
            cv2.circle(frame,centre,20,(0,0,0),4)

    
    cv2.imshow('cam',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows() 