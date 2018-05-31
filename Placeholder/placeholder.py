# Bugs:
# 1. when there is more than one placeholder for the widgets
# itsn't show messages for each widget correctly
# 2. after typing somtning and disappering placeholder cursor not
# click on roght position its move to the 0th position.
# 1test commend



from tkinter import *
from tkinter import ttk


_flag = True  # if placeholder exsist this flag will be true otherwise False

# on_click event
def onclick(event):
	global _flag

	# if there is a placeholder cursor should be move postion 0
	if _flag:
		event.widget.icursor(0)  # cursor move to postion 0
	
	# if there isn't any placeholder cursor will do it's normal job
	
# key press to on_remove placeholder message
def key_press(event):
	global _flag

	# if user type somthing when placeholder exsist 
	if _flag:
		event.widget.delete(0, END)  # delete placeholder
		event.widget.configure(foreground='black')  # text should be black
		_flag = False  # that's mean there isn't placeholder anymore.
		

def on_remove(event, message=''):
	global _flag
	content_len = len(event.widget.get())

	# if there is a placeholder
	if _flag:
		event.widget.icursor(0)  # move the cursor to position 0
		return 'break'  # don't remove any chars.

	# display placeholder message if nothing was in the inside of widget.
	elif not _flag and content_len < 1:
		event.widget.delete(0, END)  # delete text of the widget
		event.widget.insert(0, message)  # insert placeholder message
		event.widget.icursor(0)  # move cursor to position 0
		event.widget.configure(foreground= "gray")
		_flag = True

	print(_flag)


# Add placeholder to the widget.
def placeholder(widget=None, message=''):
	global _flag
	_flag = True  # There is a placeholder

	message = message.strip()
	message = ' ' + message + ' '
	widget.insert(0, message)  # insert the message to the widget
	widget.icursor(0)  # move the cursor to the first index
	widget.configure(foreground = "gray")  # make the text Gray

	# creating custom event order
	# PostRemove and PostClick will be evaluvate after default event("TEntry")
	widget.bindtags(( str(widget), "TEntry", "PostRemove", "PostClick", ".", "all"))
	widget.bind_class("PostClick", "<1>", onclick)
	widget.bind_class("PostRemove", "<BackSpace>", lambda e: on_remove(e, message))
	# widget.bind_class("PostRemove", "<Delete>", lambda e: on_remove(e, message))
	widget.bind("<Key>", key_press)
	# widget.bind("<Tab>", on_remove)


