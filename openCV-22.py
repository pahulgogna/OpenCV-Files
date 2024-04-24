import cv2
import face_recognition as FR

height = 360
width = 640

font = cv2.FONT_HERSHEY_SIMPLEX

donimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/known/Donald Trump.jpg')  # we load the image for training
FaceLoc = FR.face_locations(donimage)  # here we detect faces in the loaded image
donEncode = FR.face_encodings(donimage,FaceLoc)[0]

Seemaimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/known/Seema Verma.jpg')  # we load the image for training
FaceLoc = FR.face_locations(Seemaimage)  # here we detect faces in the loaded image
SeemaEncode = FR.face_encodings(Seemaimage,FaceLoc)[0]

Penceimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/known/Mike Pence.jpg')  # we load the image for training
FaceLoc = FR.face_locations(Penceimage)  # here we detect faces in the loaded image
PenceEncode = FR.face_encodings(Penceimage,FaceLoc)[0]

# Penceimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/known/Mike Pence.jpg')  # we load the image for training
# FaceLoc = FR.face_locations(Penceimage)  # here we detect faces in the loaded image
# PenceEncode = FR.face_encodings(Penceimage,FaceLoc)[0]

# Penceimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/known/Mike Pence.jpg')  # we load the image for training
# FaceLoc = FR.face_locations(Penceimage)  # here we detect faces in the loaded image
# PenceEncode = FR.face_encodings(Penceimage,FaceLoc)[0]

# Penceimage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/known/Mike Pence.jpg')  # we load the image for training
# FaceLoc = FR.face_locations(Penceimage)  # here we detect faces in the loaded image
# PenceEncode = FR.face_encodings(Penceimage,FaceLoc)[0]

KnownEncodings = [donEncode,SeemaEncode,PenceEncode]
names = ['Donald Trump','Seema Verma','Mike Pence']

unknownImage = FR.load_image_file('C:/Users/hukam mere aaka/python/demoImages/unknown/u6.jpg')
unknownImageBGR = cv2.cvtColor(unknownImage,cv2.COLOR_RGB2BGR)
unknown_faceLocs = FR.face_locations(unknownImage)
unknownEncodings = FR.face_encodings(unknownImage,unknown_faceLocs)

for encoding,faceLoc in zip(unknownEncodings,unknown_faceLocs):
    top,right,bottom,left = faceLoc
    matches = FR.compare_faces(KnownEncodings,encoding)
    print(matches)
    if True in matches:
        MatchIndex = matches.index(True)
        name = names[MatchIndex]
        print(name)
        cv2.rectangle(unknownImageBGR,(left,top),(right,bottom),(255,255,255),2)
        cv2.putText(unknownImageBGR,name,(left,top),font,.75,(0,0,0),2)

resized = cv2.resize(unknownImageBGR,(width,height))
cv2.imshow('img',resized)
cv2.moveWindow('img',0,0)
cv2.waitKey(10000)

