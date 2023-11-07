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