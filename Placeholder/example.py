from tkinter import *
from tkinter import ttk
from placeholder import placeholder


def on_del(event):
    return 'break'

# Some test
if __name__ == "__main__":
    # test placeholder
    root = Tk()
    var = StringVar()

    e = ttk.Entry(root)
    e.pack()
    placeholder(e, 'First placeholder ...')

    # e1 = ttk.Entry(root)
    # e1.pack()
    # placeholder(e1, 'Second placeholder ...')

    b = ttk.Button(root, text="Button")
    b.pack()
    b.focus()

    for child in root.winfo_children():
        child.pack_configure(padx=5, pady=5)

    ex = ttk.Entry(root)
    ex.pack()
    ex.insert(0, 'fuck')
    ex.bindtags(( str(ex), "TEntry", "x" ".", "all"))

    ex.bind_class("x","<BackSpace>", on_del)

    root.mainloop()
