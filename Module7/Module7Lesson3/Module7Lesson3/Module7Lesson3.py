#*******************Tkinter Notes cont...***********************
"""
Grid geometry manager:
Uses rows and columns to arrange columns.
One widget can be placed per cell unless you want one on top of 
another
"""
				#columns
		#(0,0)   (1,0)   (2,0)
		#(0,1)	 (1,1)   (2,1)
#rows	#(0,2)   (1,2)   (2,2)
		#(0,3)   (1,3)   (2,3)
			#(column, row)

"""
Grid geometry manager:
To place multiple widgets in a cell, you use a Frame or LabelFrame
- wrap the widgets
- place the Frame or LabelFrame on the cell.
The width and height of a column/row depends on the width and height
of the widget it contains.
Rows and columns can span.
"""
				#columns
		#(0,0)   (1,0)   (2,0)
		#(0,1)	 (1,1)-columnspan=2
#rows	#(0,2)   (1,2)   (2,2)
		#rowspan (1,3)   (2,3)
	#	  =2  (column, row)

"""
Configuring grid:
container.columnconfigure(index, weight)
container.rowconfigure(index, weight)
Weight determines space occupied relative to other columns/rows.
For example, a column with a weight of 2 will be twice as wide as a 
column with a weight of 1.
"""

"""
Positioning a widget
widget.grid(**options)
Parameters	Meaning
column		The column index where you want to place the widget.
row			The row index where you want to place the widget.
rowspan		Set the number of adjacent rows that the widget can span.
columnspan  Set the number of adjacent columns that the widget can 
span.
sticky		If the cell is large than the widget, the stick option 
specifies which side the widget should stick to and how to distribute 
any extra space within the cell that is not taken up by the widget at 
its original size.
padx		Add external padding above and below the widget.
pady		Add external padding to the left and right of the widget.
ipadx		Add internal padding inside the widget from the left and 
right sides.
ipady		Add internal padding inside the widget from the top and 
bottom sides.
"""

"""
Sticky:
By default, when a cell is larger than the widget it contains, the 
grid geometry manager places the widget at the center of the cell 
horizontally and vertically.
You can anchor the widget to the cardinal directions and it will 
fill in the size
"""
#Example
"""
import tkinter as tk
from tkinter import ttk
# root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
# resize values must be > 0 to resize
root.resizable(0, 0)
# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
password_entry = ttk.Entry(root, show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
root.mainloop()
"""

"""
Getting data from entry widgets:
If you want to get data from entries, you need to create and assign a
text variable to it.
entryvar1 = tk.StringVar()
entry1 = tk.Entry(window, textvariable=entryvar1)
entry1.grid(column=1, row=0)
entry1.focus()
"""

"""
Message box:

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
title = "The title"
message = "The message"
showinfo(title, message)
showerror(title, message)
showwarning(title, message)
"""

"""
Complete Examples:
Temperature Converter
Text Editor
"""
