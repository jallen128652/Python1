#***********************Tkinter Notes************************
# example -------------
"""
import tkinter

top = tkinter.Tk()

# Code to add widgets will go here...

greeting = tkinter.Label(top, text="CPT Hello")
greeting.pack()

top.mainloop()
"""

"""
Widget Constructor Syntax:

widget = WidgetName(container, **options)
Container is the parent window or frame the widget goes in.
Options are arguments for the widgets properties (font, size, color, etc.). Different
widget types can have different arguments.
"""

"""
Geometry management:
Methods to arrange your widgets around the window

message.pack()
pack() positions the window in the window and is one of the 3 geometry
management methods:
The pack() Method
The grid() Method
The place() Method
We will see these methods in a later lesson
"""

"""
Tkinter Widget Names:
Button
Canvas
Checkbutton
Entry
Frame
Label
Listbox
Menubutton
Menu
Message
Radiobutton
Scale
Scrollbar
Text
Toplevel
Spinbox
PanedWindow
LabelFrame
tkMessageBox
"""

"""
Command Binding:
(not available on all widgets)
"""
#example1

import tkinter as tk
from tkinter import ttk # allows the use of newer themed widgets
root = tk.Tk()
def button_clicked():
	print('Button clicked')
										#note command=function()call
button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack() #using pack geometry manager
root.mainloop()

#example2
import tkinter as tk
from tkinter import ttk
# create window called root
root = tk.Tk()
#put a label in the window
label = tk.Label(root, text='choose')
#position the window in the window
label.pack()
#function to output the selction to the label
def select(option):
	label['text'] = "You Chose " + option
# when you press a button the command lambda function with pass the text
# to select()
#note the command calls a lambda fx select() and assigns the string to 
#the option var being passed in
ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()
root.mainloop()

"""
Event Binding:

Not all Tkinter widgets support the command option. Tkinter provides you with an
alternative way for event binding via the bind() method.
widget.bind(event, handler, add=None)
If you want to register an additional handler, you can pass the '+' to the add
argument. It means that you can have multiple event handlers that respond to the
same event.
"""
#Event Binding
import tkinter as tk
from tkinter import ttk
def return_pressed(event):
	print('Return key pressed.')
root = tk.Tk()
btn = ttk.Button(root, text='Save')
btn.bind('<KeyPress-Return>', return_pressed)
btn.focus() # sets focus to button
btn.pack(expand=True)
root.mainloop()

#Event Binding Multiple Handlers
import tkinter as tk
from tkinter import ttk
def return_pressed(event):
 print('Return key pressed.')
def log(event):
 print(event)
root = tk.Tk()
btn = ttk.Button(root, text='Save')
btn.bind('<KeyPress-Return>', return_pressed)
btn.bind('<KeyPress-Return>', log, add='+') # add so that log 
# will not replace
btn.focus()
btn.pack(expand=True)
root.mainloop()