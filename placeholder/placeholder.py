
from tkinter import *
from tkinter import ttk


# key press to remove placeholder message
def key_press(event, style):
	# if widget contant not empty 
	#(the widget text will be placeholder message) 
	# and user type somthing
	# placeholder message will remove and keypress unbinded.
	if event.widget.get() != '':
		event.widget.delete(0, END)
		style.configure("firstpress.TEntry", foreground="black")
		event.widget['style'] = "firstpress.TEntry"
		event.widget.unbind("<Key>")


def remove(event, style=None, message=''):
	# len of text of the widget
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
		style.configure("remove.TEntry", foreground="gray")  # style the widget text to gray
		event.widget['style'] = "remove.TEntry"  # display style of the widget
		event.widget.bind("<Key>", lambda e: key_press(e, style))  # bind the key event again.


# on click event handler.
# When click inside the widget cursor 
# should move to position zerro.
def onclick(event):
	event.widget.icursor(0)


# Add placeholder to the widget.
def placeholder(widget=None, message=''):
	print(str(widget), dir(widget))
	message = message.strip()
	message = ' ' + message + '  '
	# insert the message to the widget	
	widget.insert(0, message)
	# move the cursor to the first index
	widget.icursor(0)


	# creating custom event order
	# PostRemove and PostClick will be evaluvate after default event("TEntry")
	widget.bindtags(( str(e), "TEntry", "PostRemove", "PostClick", ".", "all"))
	widget.bind_class("PostClick", "<1>", onclick)
	widget.bind_class("PostRemove", "<BackSpace>", lambda e: remove(e,s, message))
	widget.bind_class("PostRemove", "<Delete>", lambda e: remove(e,s, message))
	widget.bind("<Key>", lambda e: key_press(e, s))
	widget.bind("<Tab>", remove)


if __name__ == "__main__":
	# test placeholder
	root = Tk()
	var = StringVar()

	e = ttk.Entry(root, exportselection=0)
	e.pack()

	b = ttk.Button(root, text="Button")
	b.pack()
	b.focus()

	placeholder(e, 'Enter your name ...')

	for child in root.winfo_children():
		child.pack_configure(padx=5, pady=5)
	root.mainloop()