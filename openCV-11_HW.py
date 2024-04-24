import cv2

# -------------------------------------------------------- MouseClick function
evt = 0
def MouseClick(event,xPos,yPos,flags,params):
    global evt 
    global startPos
    global endPos
    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        startPos = (xPos,yPos)
    if event == cv2.EVENT_LBUTTONUP:
        evt = event
        endPos = (xPos,yPos)
    if event == cv2.EVENT_RBUTTONUP:
        evt = event

#------------------------------------------------------- accessing the webcam
MyCam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width = 620
height = 360
MyCam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
MyCam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
MyCam.set(cv2.CAP_PROP_FPS, 30)
MyCam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
# --------------------------------------------------------

cv2.namedWindow('Cam 1')

cv2.setMouseCallback('Cam 1', MouseClick)

while True:
    
    _, frame = MyCam.read()


    if evt == 4:
        if startPos[0] < endPos[0]:
            if startPos[1] < endPos[1]:
                frameROI = frame[startPos[1]:endPos[1],startPos[0]:endPos[0]]
            elif startPos[1] > endPos[1]:
                frameROI = frame[endPos[1]:startPos[1],startPos[0]:endPos[0]]
        elif startPos[0] > endPos[0]:
            if startPos[1] < endPos[1]:
                frameROI = frame[startPos[1]:endPos[1],endPos[0]:startPos[0]]
            elif startPos[1] > endPos[1]:
                frameROI = frame[endPos[1]:startPos[1],endPos[0]:startPos[0]]
        cv2.imshow('ROI', frameROI)
        cv2.moveWindow('ROI', width+50,0)
    if evt == 5:
        cv2.destroyWindow('ROI')
        evt = 0


    cv2.imshow('Cam 1', frame)
    cv2.moveWindow('Cam 1',0,0)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break

MyCam.release