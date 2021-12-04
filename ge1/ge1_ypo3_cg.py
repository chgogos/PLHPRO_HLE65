astring = ""  # αρχικοποίηση συμβολοσειράς
char_position = -1  # αρχικοποίηση χαρακτήρα αναζήτησης

# ερώτημα α)
while astring == "":  # αμυντικός προγραμματισμός για μη κενή συμβολοσειρά
    astring = input("Parakalw eisagete symvoloseira: ")  # είσοδος

# ερώτημα β)
while char_position == -1 or char_position > len(astring):  # αμυντικός προγραμματισμός
    char_position = int(
        input("Parakalw eisagete thn thesi tou xaraktira pros afairesi: ")
    )  # είσοδος
    print(
        astring[: char_position - 1] + astring[char_position:]
    )  # εκτύπωση συμβολοσειράς εξαιρουμένου του χαρακτήρα στην θέση char_position

# ερώτημα γ)
achar = input("Parakalw eisagete charaktira: ")  # είσοδος χαρακτήρα
charcount = astring.count(achar)  # πλήθος εμφανίσεων χαρακτήρα
print(charcount)  # εκτύπωση πλήθους εμφανίσεων χαρακτήρα
print(charcount / len(astring))  # εκτύπωση ποσοστού
