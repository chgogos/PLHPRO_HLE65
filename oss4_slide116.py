import tkinter

def b1pushed():
    name = e1.get()
    myText.set("User: "+name)
    return

w1 = tkinter.Tk()
tkinter.Label(w1,text="Type your name:").pack()
e1 = tkinter.Entry(w1)
e1.pack()
tkinter.Button(w1,text="OK",command=b1pushed).pack()
myText = tkinter.StringVar()
myText.set("Unknown user")
tkinter.Label(w1,textvariable=myText).pack()
w1.mainloop()
