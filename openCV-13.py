import cv2
print(cv2.__version__)

xAxis = 0
yAxis = 0
xCam = 0
yCam = 0

def SizeChange(val):
    global Newwidth
    Newwidth = val

def xPos(val):

    global xAxis
    xAxis = val

def yPos(val):
    global yAxis
    yAxis = val

def xCamPos(val):
    global xCam 
    xCam = val

def yCamPos(val):
    global yCam
    yCam = val

width=1280
Newwidth = 1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Controls')
cv2.resizeWindow('Controls',300,200)


cv2.createTrackbar('Size', 'Controls', width, 1920,SizeChange)
cv2.createTrackbar('xPos', 'Controls', 0, 1920,xPos)
cv2.createTrackbar('yPOS', 'Controls', 0, 1080,yPos)
cv2.createTrackbar('CamPosX', 'Controls', 0,1080,xCamPos)
cv2.createTrackbar('CamPosY', 'Controls', 0,1080,yCamPos)

cv2.namedWindow('my WEBcam')

while True:
    ignore,  frame = cam.read()

    Newheight = int((9/16)*Newwidth)

    cv2.resizeWindow('my WEBcam',Newwidth,Newheight)

    cv2.imshow('my WEBcam', frame[yCam:,xCam:])
    cv2.moveWindow('my WEBcam',xAxis,yAxis)
    cv2.moveWindow('Controls',width-50,0)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break

cam.release()