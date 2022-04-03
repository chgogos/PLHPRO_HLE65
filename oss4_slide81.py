import numpy as np
def myFun(x,y):
  return 2+x+y

arr1 = np.fromfunction(myFun,(3,3), dtype=int)
print(arr1,'\n')
print('Άθροισμα, ανα γραμμή:',arr1.sum(axis=1),' | ανα στήλη:',arr1.sum(axis=0),'\n')
print('Μέγιστο, ανα γραμμή:',arr1.max(axis=1),' | ανα στήλη:',arr1.max(axis=0),'\n')
print('Ελάχιστο, ανα γραμμή:',arr1.min(axis=1),' | ανα στήλη:',arr1.min(axis=0),'\n')

arr2 = arr1*1/2
print(arr2)