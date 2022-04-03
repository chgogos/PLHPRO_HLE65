import numpy as np
arr = np.array( [1.0, 2.0, 3.0, 4.0, 5.0])#πίνακας δεκαδικών αριθμών
print(arr)

import numpy as np
#Δημιουργία πίνακα διάστασης 4x4 με ανάθεση τιμών από 0 ως 15 ανά γραμμή
arr = np.arange(16).reshape(4,4)
print(arr)

import numpy as np
arr = np.zeros((2,4), dtype=np.float64)
#αρχικοποίηση μηδενικού πίνακα 3x4
print(arr)

import numpy as np

arr = np.empty([2,4])
print(arr)

import numpy as np
arr = np.fromfunction(lambda i, j: i + j, (4, 3))
#Πίνακας 4x3 όπου κάθε στοιχείο προκύπτει από το άθροισμα των δεικτών γραμμής και στήλης
print(arr)

import numpy as np
arr1 = np.random.randint(1,10,[3,3])
print(arr1,'\n')

arr2 = np.random.choice([3, 5, 7, 9], [3,3])
print(arr2,'\n')

arr3 = np.random.rand(2,3)
print(arr3)

arr4 = np.random.uniform([0,10], [3,3])
print(arr4)