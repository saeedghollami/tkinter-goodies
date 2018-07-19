import tkinter as tk
from tkinter import ttk
from tkinter import font


class LinkedLabel(ttk.Label):
    
    def __init__(self, master=None, **kw):
        ttk.Label.__init__(self, master=None, **kw)
        self.config(foreground='blue')
        
        f = font.Font(self, self.cget("font"))
        f.config(underline=1, weight='bold')
        print(f.configure())
       

ttk.LinkedLabel = LinkedLabel


if __name__ == "__main__":
    root = tk.Tk()
    ttk.Label(root, text="Regular Label").grid(row=0, column=1)
    ttk.LinkedLabel(root, text="Linked Label").grid(row=1, column=1)
    
    root.mainloop()
