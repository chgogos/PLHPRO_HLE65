a = 42
b = 3.141592
c = "Hello"

# classic
print("a=%d, b=%f, c=%s" % (a, b, c))

# string format() method
print("a={}, b={}, c={}".format(a, b, c))

# f-strings
print(f"a={a}, b={b}, c={c}")