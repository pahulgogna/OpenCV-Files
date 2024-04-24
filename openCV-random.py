import cv2
import numpy as np
import random

NoPixel = 3
height = 500
width = 1500
maxHue = 180

hsv = np.zeros((height,width,NoPixel),dtype=np.uint8)
hsv = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

for i in range(0,width):
    # hsv[i:i+20,int(i)] = (random.randint(0,255),random.randint(0,255), random.randint(0,255))  
    frac = int((i/width)*255)
    hsv[:,int(i)] = (frac,0,frac) 

while True:

    cv2.imshow('np', hsv)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break