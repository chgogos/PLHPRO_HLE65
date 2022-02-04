class Car:
    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st

    def __str__(self):
        return self.color + " " + self.style

    def __del__(self):
        print("Car {} destroyed".format(self.id))


c1 = Car(1, "Οικογενειακό", "Πράσινο")

print(c1)

del c1

print(c1)
