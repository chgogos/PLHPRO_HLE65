class Car:
    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st


c1 = Car(1, "Οικογενειακό", "Πράσινο")
c2 = Car(1, "Οικογενειακό", "Πράσινο")
print(c1 == c2)

print("c1: " + str(id(c1)) + " - c2: " + str(id(c2)))

c3 = c1
print(c1 == c3)

print("c1: " + str(id(c1)) + " - c3: " + str(id(c3)))

c1.color = "Κόκκινο"
print("c1 color: " + c1.color)

print("c3 color: " + c3.color)
