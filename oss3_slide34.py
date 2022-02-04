class Vehicle:
    def description(self):
        print("I'm a Vehicle!")


class Car(Vehicle):
    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st


v1 = Vehicle()
print(v1.description())

c1 = Car(1, "Οικογενειακό", "Πράσινο")
print(c1.description())
