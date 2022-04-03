import pickle
dictionary = {'Greece':'Athens',
              'Germany':'Berlin',
              'Italy':'Rome'}
f = open('countries','wb')
pickle.dump(dictionary, f)
f.close()

import pickle
f = open('countries','rb')
mydict = pickle.load(f)
print(mydict, type(mydict))

f.close()
