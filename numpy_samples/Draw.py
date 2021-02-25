## Basics of numpy 

import numpy as np
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("DATA/00-puppy.jpg")

img = cv.cvtColor(img, cv.COLOR_RGB2BGR) # for PLT

blank = np.zeros((500,500,3), np.int16) 

cv.rectangle(img,(5,5), (250,250), color=(255,255,0), thickness=5)

cv.circle(img, (250,250), 100, color=(255,0,0), thickness=5)

cv.line(img, (0,0), (250,250), color=(255,255,0), thickness=5)

cv.putText(img, "Puppy", (350,350), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=4, color=(255,255, 255), thickness=3, lineType=cv.LINE_AA)

# cv.imshow("Window", img)
# cv.waitKey(0)

# PLt needs BGR img
plt.imshow(img)
plt.show()
