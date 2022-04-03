import numpy as np

arr = np.array([[5, 1, 1],
                [4, -2, 5],
                [2, 8, 8]
                ]
               )

print("Τάξη:", np.linalg.matrix_rank(arr))

print(np.linalg.det(arr),'\n')#Ορίζουσα πίνακα

print(np.linalg.inv(arr),'\n')#Αντίστροφος πίνακας

idiotimes, idiodianismata = np.linalg.eigh(arr) # Ιδιοτιμές και ιδιοδιανύσματα
print(idiotimes,idiodianismata,'\n')