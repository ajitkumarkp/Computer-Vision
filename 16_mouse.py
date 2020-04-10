## Basics of numpy 

import numpy as np
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("00-puppy.jpg")

##################
# def call back 
##################
def mouse_callback(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img, center=(x,y), radius=10, color=(255,255,0))
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