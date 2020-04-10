import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

img = np.zeros((600,600))
cv.putText(img, "ABCDE", (50,400),cv.FONT_HERSHEY_PLAIN, 10, (255,255,255),thickness=32)

kernel= np.ones((5,5))

# Morph_gradient = erosion - dialation of the region around the edges
# This leaves you with edge detection
img_mor = cv.morphologyEx(img,cv.MORPH_GRADIENT, kernel=kernel)

cv.imshow("img",img)
cv.imshow("img_mor",img_mor)

cv.waitKey(0)
cv.destroyAllWindows()


