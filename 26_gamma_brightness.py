import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

# Gamma correction => Brighten or darken pixels.

img = cv.imread("DATA/bricks.jpg")
img = cv.cvtColor(img, cv.COLOR_RGB2BGR)/255

# img=img.astype(np.float32)

print(img[0,0])

gamma = 1 # gamma >1 will darken the image, <1 will brighten it.
result=np.power(img, gamma)

print(result[0,0])

plt.imshow(result)
plt.show()

# cv.imshow("img",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

