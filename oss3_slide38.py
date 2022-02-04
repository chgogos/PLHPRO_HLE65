class Card:
    def __init__(self, val, sym):
        self.value = val
        self.symbol = sym
        if self.symbol in "sc":
            self.color = "Black"
        else:
            self.color = "Red"
        if self.value in "JQK":
            self.fig = True
        else:
            self.fig = False

    def __repr__(self):
        return self.value + self.symbol

    def detailed_info(self):
        print(f"Αξία={self.value} Σύμβολο={self.symbol}")
        print(f"Χρώμα={self.color} Φιγούρα={self.fig}")


c = Card("K", "d")
print(c)

c.detailed_info()
