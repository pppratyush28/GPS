import math
import numpy as np
import cv2
# x for latitude
xi = 28.753034
yi = 77.117696
xf = 28.751254
yf = 77.115487

x = math.cos(xf) * math.sin(yf-yi)
y = (math.cos(xi) * math.sin(xf)) - (math.sin(xi) * math.cos(xf * math.cos(yf-yi)))

b = math.atan2(x,y)

lati = math.radians(xi)
loni = math.radians(yi)
latf = math.radians(xf)
lonf = math.radians(yf)

a = ((math.sin((latf-lati)/2)*math.sin((latf-lati)/2))+(math.cos(lati)*math.cos(latf)*math.sin((lonf-loni)/2)*math.sin((lonf-loni)/2)))
c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
d = 6371*c

print ('x:',x)
print ('y:',y)
print ("bearing:",b)
print ("degree bearing:", math.degrees(b))
print ("distance:",d)