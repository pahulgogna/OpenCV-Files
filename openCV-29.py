import cv2

width = 1280
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

class findHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,con1=.5,con2=.5):
        self.hands = self.mp.solutions.hands.Hands(False,maxHands,con1,con2)
    def handloc(self,frame):
        MyHands = []
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result = self.hands.process(frameRGB)
        if result.multi_hand_landmarks != None:
            for hand in result.multi_hand_landmarks:
                myhand = []
                for landmarks in hand.landmark:
                    myhand.append((int(landmarks.x*width),int(landmarks.y*height)))

                MyHands.append(myhand)
                
            return MyHands

hands = findHands()

while True:
    _, frame = cam.read()

    Landmarks = hands.handloc(frame)
    
    if Landmarks != None:
        for hand in Landmarks:
            cv2.circle(frame,hand[20],20,(0,0,0),-1)
    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)

    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()