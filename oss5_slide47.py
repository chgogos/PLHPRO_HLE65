def add_arbitrary(*args): # δεν γνωρίζουμε το πλήθος των ορισμάτων
    s = 0
    for number in args:
        s += number
    return s

x = 3
y = 4
print(add_arbitrary(x, y)) #κλήση με δύο ορίσματα

z = 5
w = 6
print(add_arbitrary(x, y, z, w)) #κλήση με 4 ορίσματα
