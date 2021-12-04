ymnos = """και σαν πρώτα ανδρειωμένη, χαίρε, ω χαίρε, Ἐλευθεριά!"""
freq = {}  # λεξικό καταγραφής πλήθους εμφάνισης χαρακτήρων

for ch in ymnos:
    # if ch not in freq:
    #     freq[ch] = 1
    # else:
    #     freq[ch] += 1
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
