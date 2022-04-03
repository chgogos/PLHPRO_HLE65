import time

L=[]
start_time = time.perf_counter() # αρχή μέτρησης
for i in range(10000):
    L.append(i)
finish_time = time.perf_counter() # τέλος μέτρησης
print(len(L))
print(finish_time - start_time) # διαφορά χρόνουimport time

L=[]
start_time = time.perf_counter() # αρχή μέτρησης
for i in range(10000):
    L.append(i)
finish_time = time.perf_counter() # τέλος μέτρησης
print(len(L))
print(finish_time - start_time) # διαφορά χρόνου