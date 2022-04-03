import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8])
print(arr1)

arr2 = arr1.reshape(2,4)
print(arr2)

arr3 = arr2.reshape(-1)
print(arr3)