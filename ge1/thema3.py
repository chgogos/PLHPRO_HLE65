astring=""      # αρχικοποίηση συμβολοσειράς
char_position=-1    # αρχικοποίηση χαρακτήρα αναζήτησης

# ερώτημα (α)
while not astring: # αμυντικός προγραμματισμός για μη κενή συμβολοσειρά
    astring=input("Παρακαλώ εισάγετε μία συμβολοσειρά: ") # είσοδος 

# ερώτημα (β) 
while (char_position < 1 or char_position > len(astring)): # αμυντικός προγραμματισμός
    try:
        char_position=int(input("Παρακαλώ εισάγετε τη θέση του προς αφαίρεση χαρακτήρα \
(από 1 έως {}):".format(len(astring)))) # είσοδος
        new_string = astring[:char_position-1] + astring[char_position:]
    except: print('Παρακαλώ εισάγετε ένα αριθμό από 1 μέχρι {}'\
                  .format(len(astring))) # μήνυμα σφάλματος
print("Η νέα συμβολοσειρά: {}".format(new_string)) # εκτύπωση νέας συμβολοσειράς 

# ερώτημα (γ)
while True:
    achar=input("Παρακαλω εισάγετε έναν χαρακτήρα : ") # είσοδος χαρακτήρα
    if len(achar) == 1: break
if astring.count(achar) == 1 :fores = "φορά" 
else: fores = "φορές"  #σύνταξη της λέξης φορά/φορές για το πλήθος εμφάνισης χαρακτήρα
print("Ο χαρακτήρας {} εμφανίζεται {} {} στη συμβολοσειρά {}".format(achar, \
                                            astring.count(achar), fores, astring))
print("To ποσοστό των εμφανίσεων του χαρακτήρα {} στην αρχική συμβολοσειρά είναι {}%"\
      .format(achar, int(100*astring.count(achar)/len(astring))))