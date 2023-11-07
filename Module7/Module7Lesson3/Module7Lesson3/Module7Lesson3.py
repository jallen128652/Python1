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
"""
#text copier video example
import tkinter as tk

#fx to call
def copytext():
	entryvar2.set(entryvar1.get())
	return

#create window
window = tk.Tk()
window.title("Set text")

#config window dimensions
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(1, minsize=50, weight=1)

#create buttons frame on first column
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_cpy = tk.Button(frm_buttons, text="Copy", command=copytext)
btn_cpy.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
frm_buttons.grid(row=0, column=0, sticky="ns")

#create data frame form on second window column 
frm_data = tk.Frame(window, relief=tk.RAISED, bd=2)
frm_data.grid(row=0, column=1, sticky="ns")

#Labels and entries
label1 = tk.Label(frm_data, text='Enter Text:')
label1.grid(column=0, row=0)
entryvar1 = tk.StringVar()
entry1 = tk.Entry(frm_data, textvariable=entryvar1)
entry1.grid(column=1, row=0)
entry1.focus()

label2 = tk.Label(frm_data, text='Copied text:')
label2.grid(column=0, row=1)
entryvar2 = tk.StringVar()
entry2 = tk.Entry(frm_data, textvariable=entryvar2)
entry2.grid(column=1, row=1)

#event handler and listener fx from Tkinter
window.mainloop()

#****************************************************************8
#additional examples

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# root window
root = tk.Tk()
root.title('temperature converter')
root.geometry('300x70')
root.resizable(0, 0)


def fahrenheit_to_celsius(f):
   """ convert fahrenheit to celsius
   """
   return (f - 32) * 5/9


# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# temperature label
temperature_label = ttk.Label(frame, text='fahrenheit')
temperature_label.grid(column=0, row=0, sticky='w', **options)

# temperature entry
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# convert button


def convert_button_clicked():
   """  handle convert button click event 
   """
   try:
       f = float(temperature.get())
       c = fahrenheit_to_celsius(f)
       result = f'{f} fahrenheit = {c:.2f} celsius'
       result_label.config(text=result)
   except ValueError as error:
       showerror(title='error', message=error)


convert_button = ttk.Button(frame, text='convert')
convert_button.grid(column=2, row=0, sticky='w', **options)
convert_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()

#*************************************************************



import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
   """open a file for editing."""
   filepath = askopenfilename(
       filetypes=[("text files", "*.txt"), ("all files", "*.*")]
   )
   if not filepath:
       return
   txt_edit.delete("1.0", tk.END)
   with open(filepath, mode="r", encoding="utf-8") as input_file:
       text = input_file.read()
       txt_edit.insert(tk.END, text)
   window.title(f"simple text editor - {filepath}")

def save_file():
   """save the current file as a new file."""
   filepath = asksaveasfilename(
       defaultextension=".txt",
       filetypes=[("text files", "*.txt"), ("all files", "*.*")],
   )
   if not filepath:
       return
   with open(filepath, mode="w", encoding="utf-8") as output_file:
       text = txt_edit.get("1.0", tk.END)
       output_file.write(text)
   window.title(f"simple text editor - {filepath}")

window = tk.Tk()
window.title("simple text editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="open", command=open_file)
btn_save = tk.Button(frm_buttons, text="save as...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
