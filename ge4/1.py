import os
import pickle  # Χρήση της βιβλιοθήκης pickle για τη σειριοποίηση του λεξικού


class Store:
    """κλάση για ανάκτηση και αποθήκευση δεδομένων σε ένα αρχείο pickle"""

    def __init__(self, f):
        self.store = f

    def load(self):
        # Υποερώτημα β
        if os.path.exists(self.store):
            fp = open(self.store, "rb")
            d = pickle.load(fp)
            return d
        print(f"Δεν υπάρχει αρχείο {self.store}, θα δημιουργηθεί τώρα")
        return dict()

    def save(self, data):
        # Υποερώτημα γ
        try:
            fp = open(self.store, "wb")
            pickle.dump(data, fp)
        except OSError:
            print(f"Αποτυχία στην εγγραφή του αρχείου {self.store}")


class AddressBook:
    """κλάση για διαχείριση επαφών"""

    def __init__(self, f):
        # Yποερώτημα α
        a_store = Store(f)
        self.epafes = a_store.load()
        self.contactsManagement()
        a_store.save(self.epafes)

    def contactsManagement(self):
        """'Απλή διαχείριση επαφών με εισαγωγή νέων επαφών και εκτύπωση επαφών."""
        while True:
            reply = input(
                "πατήστε + για νέα επαφή, ? για λίστα επαφών ή <enter> για έξοδο\n>>> "
            )
            if not reply:
                break
            if reply == "+":
                name = input("όνομα: ")
                phone = input("τηλέφωνο: ")
                if name and phone:
                    self.epafes[name] = phone
                else:
                    print("παρακαλώ δώστε στοιχεία")
            elif reply == "?":
                self.showContacts()

    def showContacts(self):
        for e in sorted(self.epafes):
            print(f"{e}: {self.epafes[e]}")


if __name__ == "__main__":
    addressbookFilename = "addressbook"
    AddressBook(addressbookFilename)
