import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

car = cv.imread("DATA/car_plate.jpg")

car_cascade = cv.CascadeClassifier("DATA/haarcascades/haarcascade_licence_plate_rus_16stages.xml")

def car_plate_blur(car_img):
    car_img_copy = car_img.copy()
    cp_rects = car_cascade.detectMultiScale(car_img_copy)
    
    # x= cp_rects[0][0]
    # y= cp_rects[0][1]
    # w= cp_rects[0][2]
    # h= cp_rects[0][3]

    for x,y,w,h in cp_rects:    
        blurred = cv.medianBlur(car_img_copy[y:y+h,x:x+w], 5)
        car_img_copy[y:y+h,x:x+w] = blurred
    
    cv.imshow("blurred",car_img_copy)
    cv.imshow("Original",car_img)

car_plate_blur(car)

cv.waitKey(0)
cv.destroyAllWindows()


