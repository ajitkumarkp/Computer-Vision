import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

sep_coins = cv.imread("DATA/pennies.jpg")
sep_coins_rgb = cv.cvtColor(sep_coins, cv.COLOR_BGR2RGB)

# Median blur to remove noise
blurred = cv.medianBlur(sep_coins, 25)

# convert to GS
blurred_gs = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

# Inverse Binary thresholding to get BW image, with black bkgnd
ret, blurred_gs_bt = cv.threshold(blurred_gs, 160, 255, cv.THRESH_BINARY_INV)


# cv.CHAIN_APPROX_SIMPLE means detect optimal no of points only. eg: a square needs just 4 points.
image, contours, heirarchy = cv.findContours(blurred_gs_bt.copy(),cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

print(len(contours), type(contours))
print(heirarchy, type(heirarchy))
# In this example 3 contours are detected by findContours
# 0 - External, 1&2- Internal
#  

for i in range(len(contours)): # len(contours) is 3, i= 0,1,2
    cv.drawContours(sep_coins, contours, i, (255,0,0),thickness= 10)

# plt.subplot(1,2,1)
# plt.imshow(blurred_gs_bt, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(sep_coins)

plt.show()

