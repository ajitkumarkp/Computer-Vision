import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

# Gamma correction => Brighten or darken pixels.

# img = cv.imread("DATA/bricks.jpg")
# cv.putText(img, "bricks", (100,400),cv.FONT_HERSHEY_PLAIN, 15, (0,0,255),thickness=4)
# cv.imshow("img",img)

# Method1- using the blur() where a predefined kernel is used.
# blurred = cv.blur(img, (5,5))

# Method2- using a custom kernel
# kernel = np.ones((5,5), dtype=int)/25
# blurred=cv.filter2D(img, -1, kernel)

# Method3- using Gaussian blur- averageing the neighbouring vals.
# blurred = cv.GaussianBlur(img, (5,5), 10)

# Method4- using meidian blur- blurs the background, the text remains intact.
# blurred = cv.medianBlur(img, 5)
# cv.imshow("blurred",blurred)

# Median blurr example
img_org = cv.imread("DATA/sammy.jpg")
cv.imshow("img_org",img_org)
img_noise = cv.imread("DATA/sammy_noise.jpg")
cv.imshow("img_noise",img_noise)

blurred = cv.medianBlur(img_noise, 5)
cv.imshow("blurred",blurred)

bilateral = cv.bilateralFilter(img_noise, 9,75,75)
cv.imshow("bilateral",bilateral)




cv.waitKey(0)
cv.destroyAllWindows()


