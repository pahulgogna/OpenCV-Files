import cv2
import numpy as np

row_black = 8
column_black = 8

row_pixels = 800
column_pixels = 800
variables_in_tuple = 3

darkColor = (0,0,0)
lightColor = (125,125,0)
nowColor = darkColor

row_block_size = int(row_pixels/row_black)
column_block_size = int(column_pixels/column_black)

while True:
    frame = np.zeros([row_pixels, column_pixels, variables_in_tuple], dtype= np.uint8)

    for i in range(0,row_black):
        for j in range(0, column_black):
            frame[row_block_size*i:((i+1)*row_block_size), column_block_size*j:((j+1)*column_block_size)] = nowColor
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor

        if nowColor == darkColor:
                nowColor = lightColor
        else:
            nowColor = darkColor



    cv2.imshow('board', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break