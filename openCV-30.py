import cv2

width = 1280
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

class findHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,con1=2,con2=2):
        self.hands = self.mp.solutions.hands.Hands(False,maxHands,con1,con2)
    def handloc(self,frame):
        MyHands = []
        handsType = []
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result = self.hands.process(frameRGB)
        if result.multi_hand_landmarks != None:
            
            for handLandmarks, hand in zip(result.multi_hand_landmarks,result.multi_handedness):
                handType = hand.classification[0].label
                # print(handType)
                handsType.append(handType)
                myhand = []
                for landmarks in handLandmarks.landmark:
                    myhand.append((int(landmarks.x*width),int(landmarks.y*height)))

                MyHands.append(myhand)
                
        return MyHands, handsType

hands = findHands()
HandColor = (0,0,0)

while True:
    _, frame = cam.read()

    Landmarks,HandType = hands.handloc(frame)
    # print(hands.handloc(frame))
    if Landmarks != []:        
        for handLocation,hand in zip(Landmarks,HandType):
            if hand == 'Left':
                HandColor = (0,0,255)
            elif hand == 'Right':
                HandColor = (255,0,0)
            cv2.circle(frame,handLocation[20],20,HandColor,-1)
    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)

    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()