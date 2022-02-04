import random


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


class Deck:
    values = "A23456789TJQK"  # Όλες οι αξίες
    symbols = "shcd"  # Όλα τα σύμβολα

    def __init__(self):
        self.content = []
        for s in Deck.symbols:
            for v in Deck.values:
                c = Card(v, s)
                self.content.append(c)

    def __repr__(self):
        return str(self.content)

    def shuffle(self):
        random.shuffle(self.content)


d = Deck()
print(d)

d.shuffle()
print(d)
