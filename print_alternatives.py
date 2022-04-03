a = 42
b = 3.141592
c = "Hello"

# simple print
print(a, b, c)

# classic
print("a=%d, b=%10.2f, c=%s" % (a, b, c))

# # string format() method
print("a={}, b={}, c={}".format(a, b, c))

# # f-strings
print(f"a={a}, b={a*b:.2f}, c={c}")
