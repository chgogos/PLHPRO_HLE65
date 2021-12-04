a = [1, 2, 3, 4]
b = a
print(a, b)
print(id(a), id(b), id(a) == id(b))
a[0] = 5
print(a, b)
print(id(a), id(b), id(a) == id(b))

c = a[:] # clone
print(a, c)
print(id(a), id(c), id(a) == id(c))
a[0] = 6
print(a, c)
print(id(a), id(c), id(a) == id(c))
