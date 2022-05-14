import sqlite3  # Χρήση της βιβλιοθήκης sqlite3

DB_NAME = "library.db"


def show_records(table):  # Συνάρτηση προβολής των εγγραφών του πίνακα table
    sql = f"SELECT * from {table};"  # Ερώτημα (query) για την προβολή των εγγραφών ενός πίνακα
    # Υποερώτημα α
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    col_data = conn.execute(f"PRAGMA table_info({table});").fetchall()
    print([entry[1] for entry in col_data])
    result = cursor.execute(sql)
    for rec in result:
        print(rec)
    conn.close()


def insert_student(name, surname):  # Συνάρτηση εισαγωγής φοιτητή
    sql = "INSERT INTO students(name,surname) VALUES (?,?);"  # Ερώτημα (query) για την εισαγωγή του ονόματος (name) και επώνυμου (surname) του νέου μαθητή στον πίνακα students
    # Υποερώτημα β
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(sql, (name, surname))
    conn.commit()
    conn.close()


def delete_student(code):  # Συνάρτηση διαγραφής φοιτητή
    sql = "DELETE FROM students WHERE id==(?)"  # Ερώτημα (query) για τη διαγραφή του μαθητή βάση του κωδικού του από τον πίνακα students
    # Υποερώτημα γ
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(sql, (code,))
    if cursor.rowcount == 0:
        print(f"Αποτυχία διαγραφή φοιτητή με κωδικό {code}")
    else:
        print(f"Διαγράφηκε ο φοιτητής με κωδικό {code}")
    conn.commit()
    conn.close()


# Κυρίως πρόγραμμα

# Συμβολοσειρά με τις επιλογές του μενού
library_menu = """Επιλογές συστήματος:  
1) Προβολή μαθητών
2) Προβολή βιβλίων
3) Προβολή δανεισμών 
4) Καταχώρηση μαθητή
5) Διαγραφή μαθητή
6) Έξοδος
Η επιλογή σας: """

# Κεντρικό μενού της εφαρμογής
while True:
    entry = input(library_menu)  # Εισαγωγή επιλογής μενού
    if entry == "1":
        show_records(
            "students"
        )  # Χρήση της συνάρτησης show_records για τον πίνακα students
    elif entry == "2":
        show_records("books")  # Χρήση της συνάρτησης show_records για τον πίνακα books
    elif entry == "3":
        show_records(
            "lending"
        )  # Χρήση της συνάρτησης show_records για τον πίνακα lending
    elif entry == "4":
        on = input("Καταχώρησε το όνομα του μαθητή: \n")
        ep = input("Καταχώρησε το επώνυμο του μαθητή: \n")
        insert_student(on, ep)  # Χρήση της συνάρτησης insert_student
    elif entry == "5":
        student_code = input("Καταχώρησε τον κωδικό του μαθητή προς διαγραφή: \n")
        delete_student(student_code)  # Χρήση της συνάρτησης delete_student
    elif entry == "6":
        break
    else:
        print(
            "Λανθασμένη επιλογή. Παρακαλώ επιλέξετε 1 έως 6 \n"
        )  # Μήνυμα λάθους σε περίπτωση λανθασμένης επιλογής menu
