class Mathimatika:
    def add(self, a, b):
        s = a + b
        return s


obj = Mathimatika()
c = obj.add(10, 20)

print("1η Πρόσθεση: ", c)

e = obj.add(c, 15)
print("1η Πρόσθεση: ", e)


class Car:
    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st


c1 = Car(1, "Οικογενειακό", "Πράσινο")
print(c1.id, c1.style, c1.color)

c2 = Car(2, "Σπορ", "Κόκκινο")
print(c2.id, c2.style, c2.color)

c3 = Car(2, "Νεανικό", "Μπλε")
print(c3.id, c3.style, c3.color)
