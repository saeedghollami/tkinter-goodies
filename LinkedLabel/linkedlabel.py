import tkinter as tk
import webbrowser

from tkinter import ttk
from tkinter import font


class LinkedLabel(ttk.Label):
    


    def __init__(self, master=None, href=None, **kw):
        ttk.Label.__init__(self, master=None, **kw)

        self.href = href
        print(self.href)
        
        # make text of label be blue.
        self.config(foreground='blue')
        
        # make label text have underline
        f = font.Font(self, self.cget("font"))
        f.config(underline=True)
        self.configure(font=f)

        # binds
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<1>", self._on_click)

    def __setitem__(self, key, value):
        if key == 'href':
            self.href = value

    def __getitem__(self, key):
        return self.href

    # When mouse cursor enter the area of Label
    def _on_enter(self, event):
        self.configure(cursor='hand1')
    
    # When mouse leave the area of Label
    def _on_leave(self, event):
        pass

    # when clicked on label
    def _on_click(self, event):
        webbrowser.open(self.href)



ttk.LinkedLabel = LinkedLabel


if __name__ == "__main__":
    root = tk.Tk()
    ttk.Label(root, text="Regular Label").grid(row=0, column=1)
    ll = ttk.LinkedLabel(root, text="Linked Label", href="https://www.google.com")
    ll.grid(row=1, column=1)

    ll['href'] = 'https://www.evernote.com'
    print(ll['href'])

    root.mainloop()
