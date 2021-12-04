choice=-1 # αρχικοποίηση επιλογής
antitimo=0 # αρχικοποίηση αντιτίμου
while (choice != 0): # έλεγχος για έξοδο από το πρόγραμμα
    while ( choice < 0 or choice > 4): # εμφάνιση επιλογών
        print(" Parakalw epilekste ena apo ta parakatw")
        print(" 1. Kafe 1.5 euro")
        print(" 2. Kafe me gala 1.8 euro")
        print(" 3. Sokolata 2.1 euro")
        print(" 4. Sokolata me gala 2.4 euro")
        print(" 0. Exodos")

choice=int(input("Parakalw eisagete thn epilogh sas: ")) # είσοδος επιλογής
if (choice != 0 ):
    if (choice == 1 ):
        antitimo = 150
    elif (choice == 2 ):
        antitimo = 180
    elif (choice == 3 ):
        antitimo = 210
    elif (choice == 4 ):
        antitimo = 240
    poso = 0	# αρχικοποίηση
while (poso < antitimo):	# αρχικοποίηση
    ikerma=0
    while (ikerma != 10 and ikerma != 20 and ikerma != 50 and ikerma != 100 and ikerma != 200 and ikerma != 500 and ikerma != 1000):
        print("Prepei na eisagete","{:3.1f}".format((antitimo - poso)/100),"euro synolika")
        kerma=float(input("Posa eisagete ? "))
        ikerma = kerma * 100
        if (ikerma != 10 and ikerma != 20 and ikerma != 50 and ikerma != 100 and ikerma != 200 and ikerma != 500 and ikerma != 1000):
            print("Eisagete mia egkyrh timh: 0.1 / 0.2 / 0.5 / 1 / 2 / 5 / 10 ");
    poso += ikerma;

# υπολογισμός υπόλοιπου (ρέστα) και αριθμού κερμάτων ανά είδος κέρματος που πρέπει να επιστραφούν
    resta = poso - antitimo # υπολογισμός υπολοίπου
    print("Epistrofh", "{:3.1f}".format(resta/100), "euro") 
    if (resta): # αν υπάρχουν ρέστα
        print("Parakalw parte")
        dieura = resta // 200 # υπολογισμός επιστροφής κερμάτων 2€
        resta -= 200 * dieura # ενημέρωση υπολοίπου ποσού
        if ( dieura > 0 ):
          print(" dieura :", int(dieura))
        monoeura = resta // 100 # υπολογισμός επιστροφής κερμάτων 1€
        resta -= 100 * monoeura # ενημέρωση υπολοίπου ποσού
        if ( monoeura > 0 ):
            print(" monoeura :", int(monoeura))
        penintalepta = resta // 50 # υπολογισμός επιστροφής κερμάτων 0.5€
        resta -= 50* penintalepta # ενημέρωση υπολοίπου ποσού
        if ( penintalepta > 0 ):
            print("penintalepta :", int(penintalepta))
        eikosalepta = resta // 20 # υπολογισμός επιστροφής κερμάτων 0.2€
        resta -= 20* eikosalepta # ενημέρωση υπολοίπου ποσού
        if ( eikosalepta > 0 ):
            print(" eikosalepta :", int(eikosalepta))
        dekalepta = resta // 10 # υπολογισμός επιστροφής κερμάτων 0.1€
        if ( dekalepta > 0 ):
            print(" dekalepta :", int(dekalepta))
