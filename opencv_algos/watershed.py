import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

# 1. Read Image
img = cv.imread("DATA/pennies.jpg")

# 2.  Median blur to remove noise
img = cv.medianBlur(img, 35)

# 3. convert to GS
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 4. Inverse Binary + Otsu thresholding to get BW image, with black bkgnd
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

# 5. Find the sure background via dialation. i.e expand the fg for 3 iterations
kernel = np.ones((3,3))
sure_bg = cv.dilate(thresh, kernel, iterations=3)

# 6. Find sure FG
# Now do a distance transform to actually identify the individual objects in the foreground
# Farther you go away from black(0), the brightness values increase.
dist_transform = cv.distanceTransform(thresh, cv.DIST_L2, 5)
# Inverse Binary thresholding will give you 6 distinct points you know for sure is in the foregnd
ret, sure_fg = cv.threshold(dist_transform, 0.7* dist_transform.max(), 255, 0)

# 7. find the unknown region i.e BG-FG which is the doughnut area
sure_fg =np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)

# 8. Find the markers
ret, markers = cv.connectedComponents(sure_fg)
# plt.imshow(markers, cmap="gray")

# BG is 1
# FG is 6 differnt shades (2, 3, 4, 5, 6, 7)
# unknown is black or 0
markers = markers+1
markers[unknown==255] = 0

# plt.imshow(markers, cmap="gray")

# 9. Apply Watershed algo to the markers that represent each of the coins with diff shades (2-7)
markers = cv.watershed(img, markers)
# plt.imshow(markers, cmap="gray")

# 10. Now apply findcontours and find contours on the image that has the 6 diff shades.
image, contours, heirarchy = cv.findContours(markers.copy(),cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)): # len(contours) is 3, i= 0,1,2
    cv.drawContours(img, contours, i, (255,0,0),thickness= 10)

plt.imshow(img, cmap="gray")
plt.show()

