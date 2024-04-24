import cv2
import numpy as np

NoPixel = 3
height = 256
width = 180

nparray = np.zeros((height,width,NoPixel),dtype=np.uint8)

for j in range(0,height):
    for i in range(0,width):
            nparray[j,i] = (i, j, 255)  
x = cv2.cvtColor(nparray,cv2.COLOR_HSV2BGR)

while True:
    cv2.imshow('np', x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break