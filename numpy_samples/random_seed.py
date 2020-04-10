import numpy as np

my_array=np.zeros((1,4), int)
# print(type(my_array))


# print(type(np.arange(2,10,2)))


np.random.seed(101)
print(np.random.randint(0,100,10))
print(np.random.randint(0,100,10))
print(np.random.randint(0,100,10))

print("++++++++++++++++++++")

np.random.seed(1)
print(np.random.randint(0,100,10))
print(np.random.randint(0,100,10))
print(np.random.randint(0,100,10))

print("++++++++++++++++++++")

np.random.seed(101)
print(np.random.randint(0,100,10))
print(np.random.randint(0,100,10))
print(np.random.randint(0,100,10))
