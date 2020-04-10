import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

nadia = cv.imread("DATA/Nadia_Murad.jpg", 0)
denis = cv.imread("DATA/Denis_Mukwege.jpg", 0)
solvay = cv.imread("DATA/solvay_conference.jpg",0)

face_cascade = cv.CascadeClassifier("DATA/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("DATA/haarcascades/haarcascade_eye.xml")


def detect_face(face_img):
    face_copy = face_img.copy()
    face_rects = face_cascade.detectMultiScale(face_copy)

    for x,y,w,h in face_rects:
        cv.rectangle(face_copy, (x,y), (x+w, y+h),(255,0,0),10)
    
    return face_copy

def adj_detect_face(face_img):
    face_copy = face_img.copy()
    face_rects = face_cascade.detectMultiScale(face_copy, scaleFactor=1.2, minNeighbors=5)

    for x,y,w,h in face_rects:
        cv.rectangle(face_copy, (x,y), (x+w, y+h),(255,0,0),10)
    
    return face_copy


def detect_eyes(img):
    img_copy = img.copy()
    eye_rects = eye_cascade.detectMultiScale(img_copy)

    for x,y,w,h in eye_rects:
        cv.rectangle(img_copy, (x,y), (x+w, y+h),(255,0,0),10)
    
    return img_copy

# Unable to detect the denis's eyes because the haar cascades are based on  
# viola jones algo, which is mainly looking for a change in black-white pixels
# in this case there is very little white around his eyes due to editing. 
plt.imshow(detect_eyes(denis), cmap="gray") 
plt.show()



