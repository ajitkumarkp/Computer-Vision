import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

horse = cv.imread("DATA/horse.jpg")
rainbow = cv.imread("DATA/rainbow.jpg")
bricks = cv.imread("DATA/bricks.jpg")

horse_rgb = cv.cvtColor(horse, cv.COLOR_BGR2RGB)
rainbow_rgb = cv.cvtColor(rainbow, cv.COLOR_BGR2RGB)
bricks_rgb = cv.cvtColor(bricks, cv.COLOR_BGR2RGB)

plt.subplot(2,2,1)
plt.imshow(rainbow_rgb)

mask = np.zeros(rainbow.shape[:2], np.uint8)
# Np array indexing is [y:x]
# change these values to get diffent masks
mask[0:100, 0:50] = 255

plt.subplot(2,2,2)
# masked_rainbow =  cv.bitwise_and(rainbow, rainbow, mask=mask)
# using rgb since plt takes rgb
masked_rainbow_rgb =  cv.bitwise_and(rainbow_rgb, rainbow_rgb, mask=mask)
plt.imshow(masked_rainbow_rgb, cmap='gray')

plt.subplot(2,2,3)
# This is the histogram of the full rainbow
for i, col in [(0,"b"), (1,"g"), (2,"r")]:
    hist = cv.calcHist([rainbow], channels=[i],mask=None, histSize=[256],ranges=[0,256])
    plt.plot(hist, color=col)

plt.subplot(2,2,4)
# This is the histogram of the masked area in the rainbow
for i, col in [(0,"b"), (1,"g"), (2,"r")]:
    hist = cv.calcHist([rainbow], channels=[i],mask=mask, histSize=[256],ranges=[0,256])
    plt.plot(hist, color=col)

plt.show()



