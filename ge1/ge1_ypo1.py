term = 9  # ψηφίο βάσης
sum = 0  # μεταβλητή αθροίσματος
for i in range(1, 10):  # επανάληψη για 9 ψηφία
    sum += term  # ενημέρωση του αθροίσματος
    term = (term * 10) + 9  # ενημέρωση του όρου προς πρόσθεση
print(sum)  # εκτύπωση αθροίσματος
