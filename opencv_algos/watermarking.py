import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

dog_img = cv.imread("DATA/dog_backpack.png")
dog_img = cv.resize(dog_img, (1400,900))

watermark_img = cv.imread("DATA/watermark_no_copy.png" )
watermark_img = cv.resize(watermark_img, (1400,900))

## Method 1- In this method both images have to be of the same size
weighted = cv.addWeighted(dog_img, 0.9, watermark_img, 0.2, 0.9)

cv.imshow("wind",weighted)

## Method 2-  In this method one image is overlaid on the other
# dog_img[250:750, 250:750]= watermark_img
## Method 3-  The complicated method. Refer video 24

cv.waitKey(0)
cv.destroyAllWindows()
