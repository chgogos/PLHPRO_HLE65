import tkinter
w1 = tkinter.Tk() #Δημιουργία παραθύρου w1
w1.title("Παράδειγμα 1")
L1 = tkinter.Label(w1, text="   Hello World!  ", font="Arial 40")
L1.pack() # τοποθέτηση label L1 στο παράθυρο w1
w1.mainloop() # έναρξη βρόχου