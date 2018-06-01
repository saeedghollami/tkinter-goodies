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
# _no_keys = ("Tab", "Shift_L", "Control_L", "Control_L", "Return")
_traked_keys = (
	'1', '2', '3', '4', '5', '6', '7', '7', '8', '9', '0', 
	'minus', 'equal', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 
	'o', 'p', 'bracketleft', 'bracketright', 'backslash', 'a', 'grave',
	's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semicolon', 'apostrophe', 
	'z', 'x', 'c', 'v', 'b', 'n', 'm', 'comma', 'period', 'slash', 'space', 
	'asciitilde', 'exclam', 'at', 'at', 'numbersign', 'dollar', 'percent', 
	'asciicircum', 'ampersand', 'asterisk', 'parenleft', 'parenright', 
	'underscore', 'plus', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 
	'P', 'braceleft', 'braceright', 'bar', 'A', 'S', 'D', 'F', 'G', 'H',
	'J', 'K', 'L', 'colon', 'quotedbl', 'Z', 'X', 'C', 'V', 'B', 'N', 
	'M', 'less', 'greater', 'question',  
)


# on_click event
	# if there is a placeholder cursor should be move postion 0
def on_click(event):
	global _flag

	if _flag:
		event.widget.icursor(0)  # cursor move to postion 0


# double click event handler
# if there is a placeholder double click should move cursor to pos 0
def on_double_click(event):
	global _flag

	if _flag:
		event.widget.icursor(0)
		return 'break'


# key press event handler
def key_press(event):
	global _flag

	keysym = event.keysym
	keycode = event.keycode

	# if user type somthing when placeholder exsist 
	# and user typed keycode is between 10 and 61
	if _flag and keysym in _traked_keys:
		event.widget.delete(0, END)  # delete placeholder
		event.widget.configure(foreground='black')  # text should be black
		_flag = False  # that's mean there isn't placeholder anymore.


	print(keysym.__repr__(), keycode, _flag)

def on_backspace(event, message=''):
	global _flag
	content_len = len(event.widget.get())

	# if there is a placeholder
	if _flag:
		event.widget.icursor(0)  # move the cursor to position 0
		return 'break'  # don't run default event handler.

	# display placeholder message if nothing is inside of widget.
	elif content_len < 1:
		event.widget.delete(0, END)  # delete text of the widget
		event.widget.insert(0, message)  # insert placeholder message
		event.widget.icursor(0)  # move cursor to position 0
		event.widget.configure(foreground= "gray")
		_flag = True


# Delete key event handler
def on_delete(event, message):
	global _flag
	content_len = len(event.widget.get())

	if _flag:
		return 'break'

	elif content_len < 1:
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
	widget.bind_class("PostClick", "<1>", on_click)
	widget.bind_class("PostRemove", "<BackSpace>", lambda e: on_backspace(e, message))
	widget.bind_class("PostRemove", "<Delete>", lambda e: on_backspace(e, message))
	widget.bind("<Double-Button-1>", on_double_click)
	widget.bind("<Key>", key_press)


