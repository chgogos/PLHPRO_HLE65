class Car:
    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st

    def get_obj_info(self):
        return str(self.id) + " - " + str(self.color) + " - " + str(self.style)


c1 = Car(1, "Οικογενειακό", "Πράσινο")
print(c1.get_obj_info())

c2 = Car(2, "Σπορ", "Κόκκινο")
print(c2.get_obj_info())

c3 = Car(2, "Νεανικό", "Μπλε")
print(c3.get_obj_info())
