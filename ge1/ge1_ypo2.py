x=-1 # αρχικοποίηση
while (x <=0): # αμυντικός προγραμματισμός ώστε να είναι θετικός αριθμός
    x=int(input("Dwse ton akeraio arithmo: "))	# εισαγωγή αριθμού
y=list(str(x))	# μετατροπή μεταβλητής 
total=0		# αρχικοποίηση αθροίσματος
for element in y:	# διατρέχουμε τα ψηφία
    total += int(element)	# ενημέρωση του αθροίσματος
print(total)	# εκτύπωση αθροίσματος
