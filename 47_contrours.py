import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

img_bgr = cv.imread("DATA/internal_external.png")

img = cv.imread("DATA/internal_external.png", 0)

# cv.RETR_CCOMP for both internal and external contours
# image is same as img
# contours is list of lists for all the points forming the contour
# heirarchy is an ndarray 
image, contours, heirarchy = cv.findContours(img, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

# print(len(contours)) # i.e detected 22 contours
# print(type(contours)) # is Lists
# print(contours[0][0]) # is [[247 322]] i,e one pixel value
# print(len(heirarchy))  # is 1
# print(type(heirarchy)) # is nympy.ndarray
# print(heirarchy[0][0][3]) #is -1

for i in range(len(contours)): # loop 22 times for each contour
    # -1 is external contour
    # non -1 is internal contours. 0/4 represent the groupings of internal 
    if heirarchy[0][i][3] == -1: # external
        cv.drawContours(img_bgr, contours,i,(255,0,0), thickness=5)
    else: # internal
        cv.drawContours(img_bgr, contours,i,(0,0,255), thickness=5)
    
plt.imshow(img_bgr)
plt.show()