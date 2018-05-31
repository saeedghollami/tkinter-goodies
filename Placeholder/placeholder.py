# Bugs:
# 1. when there is more than one placeholder for the widgets
# itsn't show messages for each widget correctly
# 2. after typing somtning and disappering placeholder cursor not
# click on roght position its move to the 0th position.
# 1test commend



from tkinter import *
from tkinter import ttk


_flag = True  # if placeholder exsist this flag will be true otherwise False

# the keys didn't remove placeholder when it exisit
_no_keys = ("Tab", "Shift_L", "Control_L", "Control_L", "Return")


def press_tab(event):
	print(dir(event), event.keysym, event.keycode)
# on_click event
def on_click(event):
	global _flag

	# if there is a placeholder cursor should be move postion 0
	if _flag:
		event.widget.icursor(0)  # cursor move to postion 0
	
	# if there isn't any placeholder cursor will do it's normal job
	
# key press to on_remove placeholder message
def key_press(event):
	global _flag

	keysym = event.keysym
	keycode = event.keycode

	# if user type somthing when placeholder exsist 
	# and user typed keycode is between 10 and 61
	if _flag and 9 < keycode < 62 and keysym not in _no_keys:
		event.widget.delete(0, END)  # delete placeholder
		event.widget.configure(foreground='black')  # text should be black
		_flag = False  # that's mean there isn't placeholder anymore.

	# if keysym is up down right left key
	elif 110 < keycode < 115:
		return 'break'    # do not call defualt event handler

	print(keysym, keycode)
	

def on_remove(event, message=''):
	global _flag
	content_len = len(event.widget.get())

	# if there is a placeholder
	if _flag:
		event.widget.icursor(0)  # move the cursor to position 0
		return 'break'  # don't run default event handler.

	# display placeholder message if nothing was in the inside of widget.
	elif content_len < 1:
		event.widget.delete(0, END)  # delete text of the widget
		event.widget.insert(0, message)  # insert placeholder message
		event.widget.icursor(0)  # move cursor to position 0
		event.widget.configure(foreground= "gray")
		_flag = True


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
	widget.bind_class("PostClick", "<1>", on_click)
	widget.bind_class("PostRemove", "<BackSpace>", lambda e: on_remove(e, message))
	widget.bind_class("PostRemove", "<Delete>", lambda e: on_remove(e, message))
	widget.bind("<Key>", key_press)


