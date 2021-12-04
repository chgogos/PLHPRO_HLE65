from functools import reduce

print(reduce(lambda a,b:a+b, [int('9' * i) for i in range(1,10)]))