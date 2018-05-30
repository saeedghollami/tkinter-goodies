# Bugs:
# 1. when there is more than one placeholder for the widgets
# itsn't show messages for each widget correctly
# 2. after typing somtning and disappering placeholder cursor not
# click on roght position its move to the 0th position.




from tkinter import *
from tkinter import ttk


# on_click event
def onclick(event):
	event.widget.icursor(0)


# key press to on_remove placeholder message
def key_press(event):

	if event.widget.get() != '':
		event.widget.delete(0, END)
		event.widget.configure(foreground='black')
		event.widget.unbind("<Key>")


def on_remove(event, message=''):
	content_len = len(event.widget.get())

	# if placeholder message was the text of the widget , deactive
	# Backspace, Delete and Tab keys function.
	if event.widget.get() == message:
		event.widget.icursor(0)  # move the cursor to position 0
		return 'break'  # deactive the default event action.

	# display placeholder message if nothing was in the inside of widget.
	elif content_len < 1:
		event.widget.delete(0, END)  # delete text of the widget
		event.widget.insert(0, message)  # insert placeholder message
		event.widget.icursor(0)  # move cursor to position 0
		event.widget.configure(foreground= "gray")
		event.widget.bind("<Key>", key_press)  # bind the key event again.


# Add placeholder to the widget.
def placeholder(widget=None, message=''):
	message = message.strip()
	message = ' ' + message + '  '
	widget.insert(0, message)  # insert the message to the widget
	widget.icursor(0)  # move the cursor to the first index
	widget.configure(foreground = "gray")  # make the text Gray

	# creating custom event order
	# PostRemove and PostClick will be evaluvate after default event("TEntry")
	widget.bindtags(( str(e), "TEntry", "PostRemove", "PostClick", ".", "all"))
	widget.bind_class("PostClick", "<1>", onclick)
	widget.bind_class("PostRemove", "<BackSpace>", lambda e: on_remove(e, message))
	widget.bind_class("PostRemove", "<Delete>", lambda e: on_remove(e, message))
	widget.bind("<Key>", key_press)
	widget.bind("<Tab>", on_remove)


# Some test
if __name__ == "__main__":
	# test placeholder
	root = Tk()
	var = StringVar()

	e = ttk.Entry(root)
	e.pack()
	placeholder(e, 'First placeholder ...')

	e1 = ttk.Entry(root)
	e1.pack()
	placeholder(e1, 'Second placeholder ...')

	b = ttk.Button(root, text="Button")
	b.pack()
	b.focus()

	for child in root.winfo_children():
		child.pack_configure(padx=5, pady=5)


	root.mainloop()