import cv2

width = 80
height = 174

posX = 1
posY = 1

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:                       
    ignore, frame = cam.read()         

    cv2.imshow('my WebCam1',frame) 
    cv2.moveWindow('my WebCam1', (posX),(posY))

    cv2.imshow('my WebCam2',frame) 
    cv2.moveWindow('my WebCam2', (posX+2*width),(posY))

    cv2.imshow('my WebCam3',frame) 
    cv2.moveWindow('my WebCam3', (posX+4*width),(posY))

    cv2.imshow('my WebCam4',frame) 
    cv2.moveWindow('my WebCam4', (posX+6*width),(posY))

    cv2.imshow('my WebCam5',frame) 
    cv2.moveWindow('my WebCam5', (posX+8*width),(posY))

    cv2.imshow('my WebCam6',frame) 
    cv2.moveWindow('my WebCam6', (posX+10*width),(posY))

    cv2.imshow('my WebCam7',frame) 
    cv2.moveWindow('my WebCam7', (posX+12*width),(posY))

    cv2.imshow('my WebCam8',frame) 
    cv2.moveWindow('my WebCam8', (posX+14*width),(posY))

    cv2.imshow('my WebCam9',frame) 
    cv2.moveWindow('my WebCam9', (posX+16*width),(posY))

    cv2.imshow('my WebCam10',frame) 
    cv2.moveWindow('my WebCam10', (posX+18*width),(posY))



    cv2.imshow('my WebCam11',frame) 
    cv2.moveWindow('my WebCam11', (posX),(posY + height))

    cv2.imshow('my WebCam12',frame) 
    cv2.moveWindow('my WebCam12', (posX+2*width),(posY + height))

    cv2.imshow('my WebCam13',frame) 
    cv2.moveWindow('my WebCam13', (posX+4*width),(posY + height))

    cv2.imshow('my WebCam14',frame) 
    cv2.moveWindow('my WebCam14', (posX+6*width),(posY + height))

    cv2.imshow('my WebCam15',frame) 
    cv2.moveWindow('my WebCam15', (posX+8*width),(posY + height))

    cv2.imshow('my WebCam16',frame) 
    cv2.moveWindow('my WebCam16', (posX+10*width),(posY + height))

    cv2.imshow('my WebCam17',frame) 
    cv2.moveWindow('my WebCam17', (posX+12*width),(posY + height))

    cv2.imshow('my WebCam18',frame) 
    cv2.moveWindow('my WebCam18', (posX+14*width),(posY + height))

    cv2.imshow('my WebCam19',frame) 
    cv2.moveWindow('my WebCam19', (posX+16*width),(posY + height))

    cv2.imshow('my WebCam20',frame) 
    cv2.moveWindow('my WebCam20', (posX+18*width),(posY + height))



    cv2.imshow('my WebCam21',frame) 
    cv2.moveWindow('my WebCam21', (posX),(posY + height*2))

    cv2.imshow('my WebCam22',frame) 
    cv2.moveWindow('my WebCam22', (posX+2*width),(posY + height*2))

    cv2.imshow('my WebCam23',frame) 
    cv2.moveWindow('my WebCam23', (posX+4*width),(posY + height*2))

    cv2.imshow('my WebCam24',frame) 
    cv2.moveWindow('my WebCam24', (posX+6*width),(posY + height*2))

    cv2.imshow('my WebCam25',frame) 
    cv2.moveWindow('my WebCam25', (posX+8*width),(posY + height*2))

    cv2.imshow('my WebCam26',frame) 
    cv2.moveWindow('my WebCam26', (posX+10*width),(posY + height*2))

    cv2.imshow('my WebCam27',frame) 
    cv2.moveWindow('my WebCam27', (posX+12*width),(posY + height*2))

    cv2.imshow('my WebCam28',frame) 
    cv2.moveWindow('my WebCam28', (posX+14*width),(posY + height*2))

    cv2.imshow('my WebCam29',frame) 
    cv2.moveWindow('my WebCam29', (posX+16*width),(posY + height*2))

    cv2.imshow('my WebCam30',frame) 
    cv2.moveWindow('my WebCam30', (posX+18*width),(posY + height*2))

    i = 3


    cv2.imshow('my WebCam31',frame) 
    cv2.moveWindow('my WebCam31', (posX),(posY + height*i))

    cv2.imshow('my WebCam32',frame) 
    cv2.moveWindow('my WebCam32', (posX+2*width),(posY + height*i))

    cv2.imshow('my WebCam33',frame) 
    cv2.moveWindow('my WebCam33', (posX+4*width),(posY + height*i))

    cv2.imshow('my WebCam34',frame) 
    cv2.moveWindow('my WebCam34', (posX+6*width),(posY + height*i))

    cv2.imshow('my WebCam35',frame) 
    cv2.moveWindow('my WebCam35', (posX+8*width),(posY + height*i))

    cv2.imshow('my WebCam36',frame) 
    cv2.moveWindow('my WebCam36', (posX+10*width),(posY + height*i))

    cv2.imshow('my WebCam37',frame) 
    cv2.moveWindow('my WebCam37', (posX+12*width),(posY + height*i))

    cv2.imshow('my WebCam38',frame)
    cv2.moveWindow('my WebCam38', (posX+14*width),(posY + height*i))

    cv2.imshow('my WebCam39',frame) 
    cv2.moveWindow('my WebCam39', (posX+16*width),(posY + height*i))

    cv2.imshow('my WebCam40',frame) 
    cv2.moveWindow('my WebCam40', (posX+18*width),(posY + height*i))

    i = 4


    cv2.imshow('my WebCam41',frame) 
    cv2.moveWindow('my WebCam41', (posX),(posY + height*i))

    cv2.imshow('my WebCam42',frame) 
    cv2.moveWindow('my WebCam42', (posX+2*width),(posY + height*i))

    cv2.imshow('my WebCam43',frame) 
    cv2.moveWindow('my WebCam43', (posX+4*width),(posY + height*i))

    cv2.imshow('my WebCam44',frame) 
    cv2.moveWindow('my WebCam44', (posX+6*width),(posY + height*i))

    cv2.imshow('my WebCam45',frame) 
    cv2.moveWindow('my WebCam45', (posX+8*width),(posY + height*i))

    cv2.imshow('my WebCam46',frame) 
    cv2.moveWindow('my WebCam46', (posX+10*width),(posY + height*i))

    cv2.imshow('my WebCam47',frame) 
    cv2.moveWindow('my WebCam47', (posX+12*width),(posY + height*i))

    cv2.imshow('my WebCam48',frame) 
    cv2.moveWindow('my WebCam48', (posX+14*width),(posY + height*i))

    cv2.imshow('my WebCam49',frame) 
    cv2.moveWindow('my WebCam49', (posX+16*width),(posY + height*i))

    cv2.imshow('my WebCam50',frame) 
    cv2.moveWindow('my WebCam50', (posX+18*width),(posY + height*i))
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()


