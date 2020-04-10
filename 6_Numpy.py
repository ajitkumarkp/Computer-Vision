## Basics of numpy 

import numpy as np

# mylist = [1,2,3,4]
# print(type(mylist))

## convert a list to a nd array
# np_list = np.array(mylist)
# print(type(np_list))

## like the range()
# print(np.arange(1, 10, 2))

## to create a 2d array of all 0s or 1s in FLOAT.
# print(np.zeros(shape=(5,5)))

# print(np.ones(shape=(5,5)))


## Generating an array with random values
## finding the min/max, their index and mean
# np.random.seed(101)
# array = np.random.randint(0,100, 10)
# print(array)
# print(array.min())
# print(array.argmax())
# print(array.mean())

# print(array.reshape((5,2)))
# print(array.reshape((2,5)))


## 2D matrices 
matrix_2d = np.arange(0,100).reshape(10,10)

# print(matrix_2d.shape)
print(matrix_2d)
print(matrix_2d[1:3,2:4])
matrix_2d[:,2:4]=0
print(matrix_2d)

matrix_2d_copy = matrix_2d.copy()
matrix_2d_copy[:,2:4] = 99

print(matrix_2d_copy)


