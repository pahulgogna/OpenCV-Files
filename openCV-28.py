import mediapipe as mp,cv2,time
width = 640
height = 480

def HandFinder(frameRGB):
    hands = mp.solutions.hands.Hands(False,2,0.5,0.5)
    MyHands = []
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for hand in results.multi_hand_landmarks:
            MyHand = []
            for Landmarks in hand.landmark:
                MyHand.append((int(Landmarks.x*width),int(Landmarks.y*height)))
            MyHands.append(MyHand)
    return MyHands
    



cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    _, frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = HandFinder(frameRGB)
    for hand in result:
        cv2.circle(frame,hand[20],10,(0,0,0),-1)

    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)

    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()
