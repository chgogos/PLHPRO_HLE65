class Car:
    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st

    def get_color(self):
        return self.color

    def change_color(self, new_color):
        self.color = new_color


c1 = Car(1, "Οικογενειακό", "Πράσινο")
print(c1.id, c1.style, c1.color)

print("Χρώμα: ", c1.get_color())

c1.change_color("Μαύρο")
print("Νέο χρώμα: ", c1.get_color())
