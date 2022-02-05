def einai_teleios(a):
    synolo = 0
    for x in range(1, a):
        if a % x == 0: synolo += x
    return synolo == a

for k in range(1, 10_001):
    if einai_teleios(k): print(k)
