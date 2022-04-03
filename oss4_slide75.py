import numpy as np
arr = np.array( [1.0, 2.0, 3.0, 4.0, 5.0]) #πίνακας δεκαδικών αριθμών
print(arr)

import numpy as np
#Δημιουργία πίνακα διάστασης 4x4 με ανάθεση τιμών από 0 ως 15 ανά γραμμή
arr = np.arange(16).reshape(4,4)
print(arr)

"""##Slide 76"""

import numpy as np
arr = np.zeros((2,4), dtype=np.float64)
#αρχικοποίηση μηδενικού πίνακα 2x4
print(arr)

import numpy as np
arr = np.fromfunction(lambda i, j: i + j, (4, 3))
#Πίνακας 4x3 όπου κάθε στοιχείο προκύπτει από το άθροισμα των δεικτών γραμμής και στήλης
print(arr)