#***********************Tkinter Notes part 2*********************
"""
Geometry management:
The pack() Method - This geometry manager organizes widgets in blocks before
placing them in the parent widget.
The grid() Method - This geometry manager organizes widgets in a table-like
structure in the parent widget. Most often used.
The place() Method - This geometry manager organizes widgets by placing 
them in a specific x,y position in the parent widget.
There are more options for pack. For sake of time let us look at the other
options that are more often used. To see more pack options see
https://docs.python.org/3/library/tkinter.html#packer-options
"""

#Creating the window geometry:
#import tkinter as tk

#root = tk.Tk()
#root.title('Tkinter Window Demo')
			## ('xAxis x yAxis + fromX + fromY') from's locate the window
#root.geometry('400x400+50+50')

#root.mainloop()

"""
Place Option:
The Tkinter place geometry manager allows you to precisely position widgets 
within its container using the (x, y) coordinate system.
widget.place(**options)
-Absolute positioning is specified by the x and y options.
-Relative positions is specified by the relx and rely options.
"""

"""
Place Width and Height Options:
-To set the absolute width and height of the widget in pixels, you use the
-width - absolute width and height of the widget in pixels
-height - absolute width and height of the widget in pixels
-relwidth and relheight options for relative width and height.
	- The relwidth and relheight has a value of a floating-point number between
   0.0 and 1.0.
	- This value represents a fraction of the width and height of the container.
"""

"""
Anchor:
-To specify the exact position of the widget, you use the anchor option.
-The value of anchor can be N, E, S, W, NW, SE,or SW.
-The anchor defaults to NW which is the upper left corner of the parent container.
"""
#example
#bg = background color for text
#fg = font color
import tkinter as tk
root = tk.Tk()
root.title('Tkinter place Geometry Manager')
label1 = tk.Label(root, text="Absolute placement", bg='red', fg='white')
label1.place(x=20, y=10)
label2 = tk.Label(root,text="Relative placement", bg='blue', fg='white')
label2.place(relx=0.75, rely=0.2, relwidth=0.5, anchor='ne')
root.mainloop()