## Basics of numpy 

import numpy as np
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("00-puppy.jpg")
ix, iy= -1,-1
down=False
##################
# def call back 
##################
def mouse_callback(event, x, y, flags, param):
    global ix, iy, down
    if event==cv.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        down=True
    elif event==cv.EVENT_MOUSEMOVE:
        if down:
            cv.rectangle(img, (ix, iy), (x,y), color=(255,0,0))
    elif event==cv.EVENT_LBUTTONUP:
        down=False
##################
# 2. set call back
##################
cv.namedWindow("wind")
cv.setMouseCallback("wind", mouse_callback)

##################
# 1. show image
##################
img = np.zeros((512,512,3))
while True:
    cv.imshow("wind", img)
    if cv.waitKey(20) & 0xFF== 27: #27 is Esc
        break

cv.destroyAllWindows()

