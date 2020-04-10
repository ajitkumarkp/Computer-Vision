
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

img = cv.imread("DATA/sudoku.jpg", 0)
cv.imshow("img",img)

sobelx= cv.Sobel(img, cv.CV_64F, 1,0, ksize=5)
# cv.imshow("sobelx",sobelx)

sobely= cv.Sobel(img, cv.CV_64F, 0,1, ksize=5)
# cv.imshow("sobely",sobely)

weighted = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
# weighted = sobelx+sobely
cv.imshow("weighted",weighted)

laplacian = cv.Laplacian(img, cv.CV_64F)
# cv.imshow("laplacian",laplacian)

ret,binaryT= cv.threshold(weighted,100,255, cv.THRESH_BINARY)
cv.imshow("BinaryT",binaryT)

cv.waitKey(0)
cv.destroyAllWindows()


