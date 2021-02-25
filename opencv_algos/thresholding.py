import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

img=cv.imread('DATA/crossword.jpg', 0)

## Binary thresholding
ret, img_bin = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
# ## Differnt types:
# # THRESH_BINARY_INV
# # THRESH_TRUNC
cv.imshow("img",img_bin)

## Adaptive thresholding
img_adpt= cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11, 0)
cv.imshow("img_adpt",img_adpt)

cv.waitKey(0)
cv.destroyAllWindows()
