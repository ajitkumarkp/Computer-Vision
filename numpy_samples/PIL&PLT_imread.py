import numpy as np

# import cv2

# from matplotlib import pyplot as plt 
import matplotlib.pyplot as plt

from PIL import Image

pic= Image.open("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\udemy\\numpy_basics\\berlin.jpg", mode='r')

pic_array= np.asarray(pic)

copy_pic_array=pic_array.copy()

# copy_pic_array[:,:,1] = 0

# print(copy_pic_array[:,:,2])
# plt.imshow(copy_pic_array[:,:])
plt.imshow(copy_pic_array[:,:])
plt.show()






