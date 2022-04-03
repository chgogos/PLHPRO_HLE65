import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = np.short(arr1)
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = np.where(arr1==3)
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
arr2 = np.array([7,8,9,10,11,12])
res = np.concatenate((arr1, arr2))
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = np.array_split(arr1,3)
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
arr2 = np.array([7,8,9,10,11,12])
res = np.dot(arr1, arr2)
print(res)