from tkinter import *
from tkinter import ttk
from placeholder import placeholder


# Some test
if __name__ == "__main__":

    root = Tk()

    ttk.Label(root, text="Name: ").pack()
    name = ttk.Entry(root)
    name.placeholder("Enter your name ...")
    name.pack()
    
    fname = ttk.Entry(root)
    fname.placeholder("Enter your family name")
    fname.pack()

    

    root.mainloop()