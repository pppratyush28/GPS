import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
x = 1
y = 1

for x in range (1,200):
    cv2.circle(img,(x,y),3,(255,0,0),0)
    cv2.waitKey(10)
    cv2.imshow('win',img)
    y = y+10

cv2.waitKey(0)