import numpy as np
import cv2
import math
import time

def calc(x,y):
    xi = 28.753034
    yi = 77.117696
    xf = x
    yf = y

    x = math.cos(xf) * math.sin(yf-yi)
    y = (math.cos(xi) * math.sin(xf)) - (math.sin(xi) * math.cos(xf * math.cos(yf-yi)))

    #bearing
    b = math.atan2(x,y)
    #co-ordinates in radian
    lati = math.radians(xi)
    loni = math.radians(yi)
    latf = math.radians(xf)
    lonf = math.radians(yf)
    #calculating distance
    a = ((math.sin((latf-lati)/2)*math.sin((latf-lati)/2))+(math.cos(lati)*math.cos(latf)*math.sin((lonf-loni)/2)*math.sin((lonf-loni)/2)))
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    d = 6371*c

    #print ('x:',x)
    #print ('y:',y)
    #print ("bearing:",b)
    #print ("degree bearing:", math.degrees(b))
    #print ("distance:",d)
    return b,d

def initialize():
img = np.zeros((5912,512,3),np.uint8)
x = 1
y = 1

for x in range (1,200):
    cv2.circle(img,(x,y),3,(255,0,0),0)
    cv2.waitKey(10)
    cv2.imshow('win',img)
    y = y+10

cv2.waitKey(0)

if __name__ == "__main__":
