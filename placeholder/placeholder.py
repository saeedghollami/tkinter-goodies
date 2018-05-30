
from tkinter import *
from tkinter import ttk


# key press to remove placeholder message
def key_press(event):
	if event.widget.get() != '':
		event.widget.delete(0, END)
		event.widget['foreground'] = 'black'
		event.widget.unbind("<Key>")


def remove(event, style=None, message=''):
	content_len = len(event.widget.get())

	# if placeholder message was the text of widget deactive,
	# Backspace, Delete and Tab keys function.
	if event.widget.get() == message:
		event.widget.icursor(0)  # move the cursor to position 0
		return 'break'  # deactive the default event action.

	# display place holder message if nothing was in the inside of widget.
	elif content_len < 1:
		event.widget.delete(0, END)  # delete text of the widget
		event.widget.insert(0, message)  # insert placeholder message
		event.widget.icursor(0)  # move cursor to position 0
		event.widget['foreground'] = 'gray'
		event.widget.bind("<Key>", lambda e: key_press(e, style))  # bind the key event again.


def on_click(event):
	event.widget.icursor(0)


# Add placeholder to the widget.
def placeholder(widget=None, message=''):

	message = message.strip()  
	message = ' ' + message + '  '  

	# if the widget is the a entry or ttk entry
	if widget.widgetName == "ttk::entry":
		# insert the message to the widget	
		widget.insert(0, message)
		widget['foreground'] = 'gray'
		
		widget.bindtags((str(widget), "TEntry", "PostRemove", "PostClick", ".", "all"))
		

	elif widget.widgetName == "entry":
		widget.insert(0, message)
		widget['foreground'] = 'gray'

		widget.bindtags((str(widget), "Entry", "PostRemove", "PostClick", ".", "all"))


	elif widget.widgetName == "text":
		print(widget.widgetName)

	else: print(widget.widgetName)	
	# move the cursor to the first index
	
	widget.icursor(0)

	# Common Events
	widget.bind_class("PostClick", "<1>", on_click)
	widget.bind_class("PostRemove", "<BackSpace>", lambda e: remove(e,s, message))
	widget.bind_class("PostRemove", "<Delete>", lambda e: remove(e,s, message))
	widget.bind("<Key>", lambda e: key_press(e, s))
	widget.bind("<Tab>", remove)


if __name__ == "__main__":
	# test placeholder
	root = Tk()
	var = StringVar()

	# Text
	text = Text(root)
	text.pack()
	# placeholder(text, "This is a placeholder inside of text widget")

	# ttk Entry
	ttk_entry = ttk.Entry(root)
	ttk_entry.pack()
	placeholder(ttk_entry, 'Enter your name ...')

	# Entry
	entry = Entry(root) 
	entry.pack()
	placeholder(entry, "This is a normal old entry")

	b = ttk.Button(root, text="Button")
	b.pack()
	b.focus()

	

	for child in root.winfo_children():
		child.pack_configure(padx=5, pady=5)
	root.mainloop()