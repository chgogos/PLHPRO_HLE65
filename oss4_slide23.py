import pickle
f = open('countries','ab')
pickle.dump(3.4,f)
f.close()

import pickle
f = open('countries','rb')
mydict = pickle.load(f)
print(mydict, type(mydict))
x = pickle.load(f)
print(x, type(x))
f.close()

import os
os.remove('countries')