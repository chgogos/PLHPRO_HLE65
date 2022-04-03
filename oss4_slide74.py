import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = arr1.reshape(2,3)
print(res)

import numpy as np
arr = np.array([[0, 1], [2, 3]])
arr.resize((1, 2))
print(arr)

arr.resize((2, 3))
print(arr)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = arr1.copy()
arr1[2] = 10
print(arr1)
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = arr1.view()
arr1[2] = 10
print(arr1)
print(res)

import numpy as np
arr1 = np.array([[1,3,2,4,6,5],[7,8,9,10,11,12]])
res0 = arr1.min(axis=0)
res1 = arr1.min(axis=1)
resx = arr1.min()
print(res0)
print(res1)
print(resx)

import numpy as np
arr1 = np.array([[1,3,2,4,6,5],[7,8,9,10,11,12]])
res0 = arr1.max(axis=0)
res1 = arr1.max(axis=1)
resx = arr1.max()
print(res0)
print(res1)
print(resx)

import numpy as np
arr1 = np.array([[1,3,2,4,6,5],[7,8,9,10,11,12]])
res0 = arr1.sum(axis=0)
res1 = arr1.sum(axis=1)
resx = arr1.sum()
print(res0)
print(res1)
print(resx)

import numpy as np
arr1 = np.array([[1,3,2,4,6,5],[7,8,9,10,11,12]])
res0 = arr1.argmax(axis=0)
res1 = arr1.argmax(axis=1)
resx = arr1.argmax()
print(res0)
print(res1)
print(resx)