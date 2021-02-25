import numpy as np 
import matplotlib.pyplot as plt 
import cv2

# cv2 return ndarray in BGR format
img=cv2.imread("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\udemy\\numpy_basics\\berlin.jpg")
## cv2 displays image in bgr format
cv2.imshow("Berlin", img)


## convert BGR to RGB, plt displays image in rgb format
# img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
# plt.imshow(img, cmap='gray')
plt.show()

print(img.shape)

# cv2.waitKey(0)
