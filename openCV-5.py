import cv2

import numpy as np

while True:

    frame = np.zeros((250,250), dtype= np.uint8)
    frame[:,:125] = 255  # 0 to 255
    cv2.imshow('cam', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

