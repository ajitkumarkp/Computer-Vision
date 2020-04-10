import numpy as np 
import cv2

img=cv2.imread("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\udemy\\numpy_basics\\berlin.jpg")

# Standard method to show until a key press
while True:
    cv2.imshow("Berlin", img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()