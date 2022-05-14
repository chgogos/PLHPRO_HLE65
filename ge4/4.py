import numpy as np  # Χρήση της βιβλιοθήκης numpy
import time as tm  # Χρήση της βιβλιοθήκης time


def internalProduct(v1, v2):
    """Τυπική υλοποίηση εσωτερικού γινομένου διανυσμάτων."""
    # Υποερώτημα α
    #
    # Υπολογισμός του γινομένου των v1 και v2 με την τυπική
    # υλοποίηση
    sum_ = 0
    for i, _ in enumerate(v1):
        sum_ += v1[i] * v2[i]
    return sum_


def internalProduct_np(v1, v2):
    # Υποερώτημα β
    #
    # Υπολογισμός του γινομένου των v1 και v2 με κλήση της dot() της numpy
    return np.dot(v1, v2)


def timeit(mode, rep, v1, v2):
    """Χρονομέτρηση επαναληπτικού υπολογισμού εσωτερικού γινομένου με την τυπική υλοποίηση"""
    # Αποθήκευση στην μεταβλητή start του χρόνο έναρξης του επαναληπτικού
    # υπολογισμού με την τυπική υλοποίηση του πολλαπλασιασμού διανυσμάτων
    start_time = tm.perf_counter()

    # Υποερώτημα γ

    # Επανάληψη πολλές φορές, ώστε η ακρίβεια του ρολογιού να μην επηρεάζει
    # το αποτέλεσμα
    for _ in range(rep):
        # Κλήση της συνάρτησης, για τον υπολογισμό του γινομένου των v1 και v2
        if mode == "τυπική υλοποίηση":
            res = internalProduct(v1, v2)
        elif mode == "numpy":
            res = internalProduct_np(v1, v2)

    # Εμφάνιση του αποτελέσματος
    print(f"Τιμή που υπολογίζει η {mode} = {res}")

    # Αποθήκευση στην μεταβλητή finish_time του χρόνου ολοκλήρωσης του
    # υπολογισμού
    finish_time = tm.perf_counter()
    # Επιστροφή χρονικού διαστήματος
    return finish_time - start_time


# Κυρίως πρόγραμμα

# Aρχικοποίηση παραμέτρων
random_num_range = 100  # το εύρος των παραγόμενων τυχαίων αριθμών
vector_size = 10000  # το πλήθος των στοιχείων ενός διανύσματος
repetitions = 5000  # ο αριθμός επαναλήψεων του υπολογισμού
# Αρχικοποίηση δύο διανυσμάτων, v1 και v2, με τυχαίους αριθμούς
v1 = np.random.randint(random_num_range, size=vector_size)
v2 = np.random.randint(random_num_range, size=vector_size)

# Υποερώτημα δ

# Υπολογισμός και εμφάνιση χρόνων αναμονής
t = timeit("τυπική υλοποίηση", repetitions, v1, v2)
t_np = timeit("numpy", repetitions, v1, v2)
print(f"Χρόνος τυπικής υλοποίησης = {t/repetitions:.6f}sec")
print(f"Χρόνος numpy = {t_np/repetitions:.6f}sec")

# Υπολογισμός και εμφάνιση του λόγου των χρόνων εκτέλεσης
print(f"Η υλοποίηση με το numpy γίνεται {t/t_np:.2f} φορές ταχύτερα")
