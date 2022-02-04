class Car:
    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st


c1 = Car(1, "Οικογενειακό", "Πράσινο")

import copy

c4 = copy.copy(c1)

print("c1: " + str(id(c1)) + " - c4: " + str(id(c4)))

c1.color = "Μαύρο"
print("c1 color: " + c1.color)

print("c4 color: " + c4.color)
