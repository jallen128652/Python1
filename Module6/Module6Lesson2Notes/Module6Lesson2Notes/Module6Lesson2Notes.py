#***************************RegEx Notes*************************
"""
Python Regular Expressions
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
You need the re module to use regular expressions
import re
"""
import re

"""
Python Regular Expressions
Before we discuss the functions lets look at a regex string
This string (in blue) looks for strings that begin with "ID" and 
end with "Texas"
It works with Metacharacters
"""


"""
Metacharacters
Metacharacters are characters with a special meaning:

Character	Description									Example	
[]	A set of characters									"[a-m]"	
\	Signals a special sequence (can also be used to escape special 
characters)												"\d"	
.	Any character (except newline character)			"he..o"	
^	Starts with											"^hello"	
$	Ends with											"planet$"	
*	Zero or more occurrences							"he.*o"	
+	One or more occurrences								"he.+o"	
?	Zero or one occurrences								"he.?o"	
{}	Exactly the specified number of occurrences			"he.{2}o"	
|	Either or	# either "falls" or "stays"				"falls|stays"	
()	Capture and group

"""
#useful links:
"""
https://www.dataquest.io/blog/regex-cheatsheet/
https://www.debuggex.com/cheatsheet/regex/python
https://learnbyexample.github.io/python-regex-cheatsheet/
https://www.pythontutorial.net/python-regex/python-regex-cheat-sheet/
"""
#example
txt = "ID1008, John Doe, Texas"
#	^ = begins with . = any characters * = zero or more occurances
# $ = ends with
#note the . with the * means you can have zero or more occurrences 
#of any character
x = re.search("^ID.*Texas$", txt)
