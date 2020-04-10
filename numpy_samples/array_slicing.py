import numpy as np


my_array = np.arange(0,100).reshape(10,10)

my_array2=my_array.copy()

print("2D Array 0-100 \n", my_array)


my_array[0:5,0:5]= 0

print("2D Array 0-100 \n", my_array)


print(my_array2[0:5,:])
print(my_array2[:,0:5])
