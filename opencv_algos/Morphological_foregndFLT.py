import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

img = np.zeros((600,600))
cv.putText(img, "ABCDE", (50,400),cv.FONT_HERSHEY_PLAIN, 10, (255,255,255),thickness=32)

# Add some black-noise to the foregnd
noise =np.random.randint(low=0, high=2, size=(600,600))*-255 

img_noise = img+noise

# print(img_noise)

# cv.imshow("img",img_noise)

# plt.imshow(noise, cmap='gray')
# plt.show()

# usually kernels are 5x5 ones matrix
kernel= np.ones((5,5))

# Morph_close is used to clear black noise in the fore background
img_mor = cv.morphologyEx(img_noise,cv.MORPH_CLOSE, kernel=kernel)

# Apply erode filter
img_mor =cv.erode(img_mor, kernel,iterations=5)

cv.imshow("img",img_noise)
cv.imshow("img_mor",img_mor)

cv.waitKey(0)
cv.destroyAllWindows()


