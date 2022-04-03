import pickle
f = open("myfile","wb")
pickle.dump(3.14, f)
pickle.dump([1,2,3], f)
f.close()

import pickle
f = open("myfile","rb")
x = pickle.load(f)
print(x, type(x))
y = pickle.load(f)
print(y, type(y))
f.close()