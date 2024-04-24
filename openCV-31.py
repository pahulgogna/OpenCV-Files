import cv2

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

height = 720
width = 1280
xPos = int(width/2)
yPos = int(height/2)
dPosX = 20
dPosY = 20
rHandLoc = int(height/2)
lHandLoc = int(height/2)
HandColor = (0,0,0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

class findHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,con1=1,con2=1):
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
                    myhand.append((int((landmarks.x)*width),int((landmarks.y)*height)))

                MyHands.append(myhand)
                
        return MyHands, handsType
    
hands = findHands()
size = 100


def rectangleRight(frame,yPos,handcolor):
    cv2.rectangle(frame,(width-20,int(yPos-size/2)),(width,int(yPos+size/2)),handcolor,-1)
    return int(yPos-size/2),int(yPos+size/2)


def rectangleLeft(frame,yPos,handcolor):
    cv2.rectangle(frame,(0,int(yPos-size/2)),(20,int(yPos+size/2)),handcolor,-1)
    return int(yPos-size/2),int(yPos+size/2)

def Showball(frame,pos):
    cv2.circle(frame,pos,30,(0,255,0),-1)

def ballMove(xPos,yPos,dPosX,dPosY,rectangleL,rectangleR):
    if yPos - 30 < 0 or yPos + 30 > height:
        dPosY = -dPosY
    if xPos -50 < 0:  # left wall
        if yPos - 30 > rectangleL[0] and rectangleL[1] > yPos + 30:
            dPosX = -dPosX
    if xPos+60 > width:
        if yPos - 30 > rectangleR[0] and rectangleR[1] > yPos + 30:
            dPosX = -dPosX
    xPos += dPosX
    yPos += dPosY

    return xPos,yPos,dPosX,dPosY

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    Landmarks,HandType = hands.handloc(frame)
    # print(hands.handloc(frame))
    if Landmarks != []:
        for handLocation,hand in zip(Landmarks,HandType):
            if hand == 'Left':
                HandColor = (0,0,255)
                lHandLoc = handLocation[8][1]
            if hand == 'Right':
                HandColor = (255,0,0)
                HandLoc = handLocation[8][1]

        rectangleRUP,rectangleRDOWN = rectangleRight(frame,rHandLoc,HandColor)
        rectangleLUP,rectangleLDOWN = rectangleLeft(frame,lHandLoc,HandColor)
        xPos,yPos,dPosX,dPosY = ballMove(xPos,yPos,dPosX,dPosY,(rectangleLUP,rectangleLDOWN),(rectangleRUP,rectangleRDOWN))

    pos = (xPos,yPos)
    Showball(frame,pos)

    cv2.imshow('screen1', frame)
    cv2.moveWindow('screen1', 0,0)

    if cv2.waitKey(1)== ord('q'):
        break
    
cv2.release()