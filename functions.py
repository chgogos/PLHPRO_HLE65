g = 34

def fun():
    a = 5
    global g 
    g = 55
    print(a, g)

fun()
print(g)