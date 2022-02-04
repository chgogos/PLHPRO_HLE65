class Car:

    counter = 0  # Μεταβλητή κλάσης

    def __init__(self, id, st, clr):
        self.id = id  # Ιδιότητα στιγμιότυπου
        self.color = clr  # Ιδιότητα στιγμιότυπου
        self.style = st  # Ιδιότητα στιγμιότυπου
        Car.counter += 1  # Ιδιότητα κλάσης

    def get_color(self):
        return self.color

    def change_color(self, new_color):
        self.color = new_color


c1 = Car(1, "Οικογενειακό", "Πράσινο")
print(c1.id, c1.style, c1.color)

c2 = Car(2, "Σπορ", "Κόκκινο")
print(c2.id, c2.style, c2.color)

c3 = Car(3, "Νεανικό", "Μπλε")
print(c3.id, c3.style, c3.color)

print("Αριθμός αυτοκινήτων:", Car.counter)
