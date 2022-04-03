# Button Widget
import tkinter

def b1pushed():
    print("Button 1 was pressed.")
    return

def b2pushed():
    w1.destroy()
    return

w1 = tkinter.Tk()
tkinter.Label(w1,text="Hello there!").pack()
tkinter.Button(w1,text="Button1",command=b1pushed).pack()
tkinter.Button(w1,text="Button2",command=b2pushed).pack()
w1.mainloop()