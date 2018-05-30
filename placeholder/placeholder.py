
from tkinter import *
from tkinter import ttk


# key press to remove placeholder message
def key_press(event):
	if event.widget.get() != '':
		event.widget.delete(0, END)
		event.widget['foreground'] = 'black'
		event.widget.unbind("<Key>")


def remove(event, message=''):
	content_len = len(event.widget.get())

	# if placeholder message was the text of widget deactive,
	# Backspace, Delete and Tab keys function.
	if event.widget.get() == message:
		event.widget.icursor(0)  
		return 'break'  # deactive the default event action.

	# display place holder message if nothing was in the inside of widget.
	elif content_len < 1:
		event.widget.delete(0, END)  # delete text of the widget
		event.widget.insert(0, message)  # insert placeholder message
		event.widget.icursor(0)  
		event.widget['foreground'] = 'gray'
		event.widget.bind("<Key>", key_press)  # bind the key event again.


def on_click(event):
	event.widget.icursor(0)


# Add placeholder to the widget.
def placeholder(widget=None, message=''):
	# to hold messages for each widget
	widget_msg = {}
	

	message = message.strip()  
	message = ' ' + message + '  '  

	# if the widget is the a entry or ttk entry
	if widget.widgetName == "ttk::entry":
		# save message of ttk entry widget
		widget_msg['ttk_entry_msg'] = message 
		# insert the message to the widget	
		widget.insert(0, message)
		widget['foreground'] = 'gray'
		
		widget.bindtags((str(widget), "TEntry", "PostRemove", "PostClick", ".", "all"))
		widget.bind_class("PostRemove", "<BackSpace>", lambda e: remove(e, widget_msg['ttk_entry_msg']))
		widget.bind_class("PostRemove", "<Delete>", lambda e: remove(e, widget_msg['ttk_entry_msg']))

	elif widget.widgetName == "entry":
		# save message of entry widget
		widget_msg['entry_msg'] = message
		widget.insert(0, message)
		widget['foreground'] = 'gray'

		widget.bindtags((str(widget), "Entry", "PostRemove", "PostClick", ".", "all"))
		widget.bind_class("PostRemove", "<BackSpace>", lambda e: remove(e, widget_msg['entry_msg']))
		widget.bind_class("PostRemove", "<Delete>", lambda e: remove(e, widget_msg['entry_msg']))

	elif widget.widgetName == "text":
		# save message text widget
		widget_msg['text_msg'] = message

	else: print(widget.widgetName)	
	# move the cursor to the first index
	
	widget.icursor(0)

	# Common Events
	widget.bind_class("PostClick", "<1>", on_click)
	widget.bind("<Key>", key_press)
	widget.bind("<Tab>", remove)

	print(widget_msg)


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