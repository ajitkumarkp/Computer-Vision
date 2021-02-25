 ## Basics of numpy 
 ## Image is represented as a 3d matrix in ndarray i.e x,y,color channel.

import numpy as np

import matplotlib.pyplot as plt

import cv2 as cv
from PIL import Image

img = Image.open("00-puppy.jpg")

# img.show()

np_arr = np.asarray(img)
arr_copy = np_arr.copy()

## Printing pixel values @ a specific coordinate 
# print("value of Red @ 0,0   :", arr_copy[0,0,0])
# print("value of Green @ 0,0 :", arr_copy[0,0,1])
# print("value of Blue @ 0,0  :" , arr_copy[0,0,2])

## Modifying the pixel values in a particular img block 
# arr_copy[200:400,250:500] = (255,0,255)
# plt.imshow(arr_copy)
# plt.show()

## Viewing individual color channels seperately in their gray scale, note the color representation used in plt is not accurate.
# plt.imshow(arr_copy[:,:,0], cmap="gray")
# plt.show()

## Making individual channels 0. 
# arr_copy[:,:,2]=0
# plt.imshow(arr_copy)
# plt.show()


#Assesment1- video9

#eg: 5x5 array where every element is 10
# print(np.ones(25).reshape((5,5))*10)

#eg: 5x5 array of random values from 0-100, max/min val
np.random.seed(101)
arr = np.random.randint(0,100,size=(5,5))
# print(arr)
# print(np.min(arr))

#eg:Using plt to show PIL or ndarray images
my_img = Image.open("00-puppy.jpg")
## Show the PIL image using plt
# plt.imshow(my_img)
# plt.show()

## Show the ndarray using plt
my_np_arr = np.asarray(my_img)
# plt.imshow(my_np_arr)
# plt.show()

## Set R,G channels to 0 and display
my_np_arr_copy = my_np_arr.copy()
my_np_arr_copy[:,:,0]=0
my_np_arr_copy[:,:,1]=0
plt.imshow(my_np_arr_copy)
plt.show()



















