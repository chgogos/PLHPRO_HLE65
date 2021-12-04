a = 0.1 + 0.1 + 0.1
print("1. ", a == 0.3)
print("2. ", a)
print(f"3.  {a:.1f}")

a = round(a, 1)
print("4. ", a)

import decimal

# https://docs.python.org/3/library/decimal.html

x = decimal.Decimal(0.1)
decimal.getcontext().prec = 1
y = x + x + x
print("5. ", y)
