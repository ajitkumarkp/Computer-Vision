
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

img = np.zeros((600,600))
cv.putText(img, "ABCDE", (50,400),cv.FONT_HERSHEY_PLAIN, 10, (255,255,255),thickness=32)
kernel= np.ones((5,5))

img_er = cv.erode(img,kernel,iterations=5)

cv.imshow("img",img)
cv.imshow("img_er",img_er)

cv.waitKey(0)
cv.destroyAllWindows()


