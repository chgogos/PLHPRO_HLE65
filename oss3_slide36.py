class Vehicle:
    def __init__(self, clr):
        self.color = clr

    def description(self):
        print("I'm a", self.color, "Vehicle")


class Car(Vehicle):
    def __init__(self, clr, st):
        super().__init__(clr)
        self.style = st

    def description(self):
        print("I'm a", self.color, self.style)


v1 = Vehicle("Κόκκινο")
c1 = Car("Μαύρο", "Σπορ")

v1.description()

c1.description()

v1.description()
