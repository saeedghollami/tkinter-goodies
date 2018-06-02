from tkinter import *
from tkinter import ttk
from placeholder import placeholder


def on_del(event):
    return 'break'

# Some test
if __name__ == "__main__":
    # test placeholder
    root = Tk()


    entry_name = ttk.Entry(root)
    entry_name.pack(pady=10, padx=5)
    # placeholder(entry_name, message="Enter your name ...")
    entry_name.placeholder("fuck")

    entry_age = ttk.Entry(root)
    entry_age.pack(pady=10, padx=5)
    # placeholder(entry_age, message="Enter your age ... ")
    entry_age.placeholder("sucks")

    

    root.mainloop()
