# Import the required libraries
from tkinter import *
from tkinter import ttk
import numpy
import pandas as pd
import os

# Create an instance of tkinter frame
win = Tk()
win.geometry("1024x450")
style = ttk.Style()
style.theme_use('clam')

# Create a Frame
frame = Frame(win)
frame.pack(pady=20)
#get file path in the system
def get_file_path():
    application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path

# Define a function for opening the file
def open_file(my_sheet):
    label.config(text="")
    try:
        df = pd.read_excel(get_file_path()+"/weatherdata.xlsx", sheet_name=my_sheet)
    except ValueError:
        label.config(text="Sheet could not be opened")
        return
    except FileNotFoundError:
        label.config(text="File Not Found")

   # Clear all the previous data in tree
    clear_treeview()

   # Add new data in Treeview widget
    tree["column"] = list(df.columns)
    tree["show"] = "headings"

   # For Headings iterate over the columns
    for col in tree["column"]:
        tree.heading(col, text=col)

   # Put Data in Rows
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tree.insert("", "end", values=row)

    tree.pack()

# Clear the Treeview Widget
def clear_treeview():
   tree.delete(*tree.get_children())


# Create a Treeview widget
tree = ttk.Treeview(frame)

entry1 = ttk.Entry(win)
entry1.pack(pady=20)

btn1 = ttk.Button(win,text="Load data", command= lambda: open_file(entry1.get()))
btn1.pack(pady=5)

# Add a Label widget to display the file content
label = Label(win, text='')
label.pack(pady=5)

open_file("Αθήνα")

win.mainloop()