# Μηχανή γεωμετρίας pack()
import tkinter as tk
root = tk.Tk()
root.geometry('200x200+200+200')
# case 1
# tk.Label(root, text='Label', bg='green').pack()
# tk.Label(root, text='Label2', bg='red').pack()
# case 2
tk.Label(root, text='Label', bg='green').pack(expand=1, fill ='y')
tk.Label(root, text='Label2', bg='red').pack(fill = 'both')
# case 3
#tk.Label(root, text='Label', bg='green').pack(expand=1)
#tk.Label(root, text='Label2', bg='red').pack(fill = 'both')
# case 4
#tk.Label(root, text='Label', bg='green').pack(fill='both', expand=1, side='left')
#tk.Label(root, text='Label2', bg='red').pack(fill='both', expand=1, side='right')
# case 5
#tk.Label(root, text='Label', bg='green').pack(fill = 'both', expand=1)
#tk.Label(root, text='Label2', bg='red').pack(fill = 'both', expand=1)
root.mainloop()