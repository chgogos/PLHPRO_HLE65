x = -1  # αρχικοποίηση
while x <= 0:  # αμυντικός προγραμματισμός ώστε να είναι θετικός αριθμός
    x = int(input("Dwse ton akeraio arithmo: "))  # εισαγωγή αριθμού
total = 0  # αρχικοποίηση αθροίσματος
for element in str(x):  # διατρέχουμε τα ψηφία
    total += int(element)  # ενημέρωση του αθροίσματος
print(total)  # εκτύπωση αθροίσματος
