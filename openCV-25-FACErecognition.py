import cv2
# import face_recognition as FR
import pickle

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

height = 360
width = 640

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

font = cv2.FONT_HERSHEY_SIMPLEX

with open('C:/Users/hukam mere aaka/python/demoImages/known/faceRecData/myData.pkl','rb') as f:
    names = pickle.load(f)
    KnownEncodings = pickle.load(f)
print(names)
print(KnownEncodings)


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
