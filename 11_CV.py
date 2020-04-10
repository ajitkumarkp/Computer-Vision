## Basics of numpy 

import numpy as np
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt

### cv reads image in BGR format
# img = cv.imread("00-puppy.jpg")

### cv supports display in BGR
# # cv.imshow("puppy", img) 
# # cv.waitKey(0)

### PIL.Image reads image in RGB format
# # img = Image.open("00-puppy.jpg") 

### convert to RGB before using plt.imshow
# img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

# plt.imshow(img_rgb)
# plt.show()


## reading in grayscale- no color channels

# img_gs = cv.imread("00-puppy.jpg", cv.IMREAD_GRAYSCALE)

# print(img_gs.shape)

# plt.imshow(img_gs, cmap="gray")
# # Without the cmap the defult color map is viridis
# # to show the color in grayscale use gray
# # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html 

# plt.show()

### Resize
# img = cv.imread("00-puppy.jpg")
# print(img.shape)
# img_resized = cv.resize(img, (2000,2000))
# print(img_resized.shape)
# plt.imshow(img_resized)
# plt.show()

## FLipping Iamges

# img = cv.imread("00-puppy.jpg")

# flipped= cv.flip(img,1)
# # 1 flips along y-axis
# # 0 flips along x-axis
# # -1 Flips along both-axis

# plt.imshow(flipped)
# plt.show()













