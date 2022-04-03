#Επίλυση γραμμικού συστήματος
#2x+y-2z=-3
#3x+z=5
#x+y-z=-2
import numpy as np

A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
Β = np.transpose(np.array([[-3,5,-2]]))
print(np.linalg.solve(A,Β))