import os
import cv2
import face_recognition as FR
import time
import pickle

names = []
faceEncodings = []

DIR = 'C:\\Users\hukam mere aaka\python\demoImages\known'
timeStart = time.time()



for root,dirs,files in os.walk(DIR):
    
    # print('root =',root)
    # print('directory =',dirs)
    # print('files =',files)
    for file in files:
        name = os.path.splitext(file)[0]
        names.append(name)
        ImgAddress = root + '\\' + file
        CurrentImage = FR.load_image_file(ImgAddress)
        faceLoc = FR.face_locations(CurrentImage)
        faceEncoding = FR.face_encodings(CurrentImage,faceLoc)
        for encoding in faceEncoding:
            faceEncodings.append(encoding)
print(names)
print(faceEncodings)
with open('myData.pkl','wb') as f:  # here 'wb' stands for write binary 
    pickle.dump(names,f)
    pickle.dump(faceEncodings,f)
timeEnd = time.time()
dt = timeEnd - timeStart
print('time taken: ',dt)