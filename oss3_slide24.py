class Car:
    """This car representation Class"""

    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st


c1 = Car(1, "Οικογενειακό", "Πράσινο")

print(c1.id, c1.style, c1.color)
