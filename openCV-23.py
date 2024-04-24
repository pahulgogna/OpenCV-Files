import cv2
import face_recognition as FR

cam = cv2.VideoCapture(0)

height = 360
width = 640

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

font = cv2.FONT_HERSHEY_SIMPLEX

pahulimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/New folder/Pahul_Webcam.jpg')  # we load the image for training
FaceLoc = FR.face_locations(pahulimage)  # here we detect faces in the loaded image
pahulEncode = FR.face_encodings(pahulimage,FaceLoc)[0]

Jaiveerimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/New folder/Jaiveer.jpg')  # we load the image for training
FaceLoc = FR.face_locations(Jaiveerimage)  # here we detect faces in the loaded image
JaiveerEncode = FR.face_encodings(Jaiveerimage,FaceLoc)[0]

Pramitimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/New folder/Pramit.jpg')  # we load the image for training
FaceLoc = FR.face_locations(Pramitimage)  # here we detect faces in the loaded image
PramitEncode = FR.face_encodings(Pramitimage,FaceLoc)[0]

Papaimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/New folder/Papa.jpg')  # we load the image for training
FaceLoc = FR.face_locations(Papaimage)  # here we detect faces in the loaded image
PapaEncode = FR.face_encodings(Papaimage,FaceLoc)[0]

Mamaimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/New folder/Mama.jpg')  # we load the image for training
FaceLoc = FR.face_locations(Mamaimage)  # here we detect faces in the loaded image
MamaEncode = FR.face_encodings(Mamaimage,FaceLoc)[0]

DadiMamaimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/New folder/DadiMama.jpg')  # we load the image for training
FaceLoc = FR.face_locations(DadiMamaimage)  # here we detect faces in the loaded image
DadiMamaEncode = FR.face_encodings(DadiMamaimage,FaceLoc)[0]

Daduimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/New folder/Dadu.jpg')  # we load the image for training
FaceLoc = FR.face_locations(Daduimage)  # here we detect faces in the loaded image
DaduEncode = FR.face_encodings(Daduimage,FaceLoc)[0]

KnownEncodings = [pahulEncode,JaiveerEncode,PramitEncode,PapaEncode,MamaEncode,DadiMamaEncode,DaduEncode]

names = ['Pahul','Jaiveer','Pramit','Papa','Mama','Dadi Mama','Dadu']

while True:
    _,unknownImage = cam.read()

    # unknownImageRGB = cv2.cvtColor(unknownImage,cv2.COLOR_BGR2RGB)
    unknown_faceLocs = FR.face_locations(unknownImage)
    unknownEncodings = FR.face_encodings(unknownImage,unknown_faceLocs)

    for encoding,faceLoc in zip(unknownEncodings,unknown_faceLocs):
        top,right,bottom,left = faceLoc
        matches = FR.compare_faces(KnownEncodings,encoding)

        if True in matches:
            print(matches)
            MatchIndex = matches.index(True)
            name = names[MatchIndex]
            print(name)
            cv2.rectangle(unknownImage,(left,top),(right,bottom),(0,0,0),2)
            cv2.putText(unknownImage,name,(left,top),font,.75,(255,255,255),2)

    cv2.imshow('cam', unknownImage)
    cv2.moveWindow('cam',0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release() 
