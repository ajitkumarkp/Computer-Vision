import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0,6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

# Read and resize image to fit within the screen
img = cv2.imread("scanned-form.jpg",1)
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# Increase contrast to get better grabcut results 
# By trial and error this gamma value seems to seperate the form from the other white patches
gamma = 20
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
img2 = cv2.LUT(img, lookUpTable)

mask = np.zeros(img.shape[:2], dtype = np.uint8) # mask initialized to PR_BG
output = np.zeros(img.shape, np.uint8)           # output image to be shown

# Since we know the form occupies most of the iamge, use a rectangle 10 pixels into the img from the borders 
rect = (10,10,img.shape[1]-10,img.shape[0]-10)

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)
cv2.grabCut(img2, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)

# mask[48:51,280:300] = 0
# cv2.grabCut(img2, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)
# plt.imshow(mask);plt.show()

mask2 = np.where((mask==1)+(mask==3), 255, 0).astype('uint8')
# cv2.imshow('Mask2', mask2)

output = cv2.bitwise_and(img2, img2, mask=mask2)

# output_gray = cv2.cvtColor(output,cv2.COLOR_RGB2GRAY)
# cv2.imshow('output', output_gray)

# finding contours 
_,contours, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print("Number of contours found = {}".format(len(contours)))

# finding areas of all contours
areas = []
for index,cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    areas.append(area)
# print(areas)

# Since we know the form occupies most of the image, use the contour with largest area
epsilon = 0.05 * cv2.arcLength(contours[np.argmax(areas)], True)
pts_src = cv2.approxPolyDP(contours[np.argmax(areas)], epsilon, True)
# print (pts_src)

# The contour pts above are in anti-clockwise order.Hence making pts_dts also anti-clockwise
pts_dst = np.array([[500, 0],[0, 0],[0, 670],[500, 670]], dtype=float)

# Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)

# Warp source image to destination based on homography
im_out = cv2.warpPerspective(img, h, (img.shape[1],img.shape[0]))

cv2.imshow("Original img", img)
cv2.imshow("Final img", im_out)
cv2.waitKey(0)
