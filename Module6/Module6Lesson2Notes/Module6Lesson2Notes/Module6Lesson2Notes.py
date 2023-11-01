#***************************RegEx Notes*************************
"""
Python Regular Expressions
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
You need the re module to use regular expressions
import re
"""
#import re

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
#txt = "ID1008, John Doe, Texas"
#	^ = begins with . = any characters * = zero or more occurances
# $ = ends with
#note the . with the * means you can have zero or more occurrences 
#of any character
#x = re.search("^ID.*Texas$", txt)

"""
Special Sequences:
Begin with \
\A Matches if the specified characters are at the beginning of the 
string "\AThe"

\b Matches if the specified characters are at the beginning or at 
the end of a word ("r" string is being treated as a "raw string") 
r"\bain" r"ain\b"

\B Matches if the specified characters are present, but NOT at the
beginning (or at the end) of a word ("r" means "raw string") 
r"\Bain" r"ain\B"

\d Returns a match where the string contains digits (numbers from 
0-9) "\d"

\D Returns a match where the string DOES NOT contain digits "\D"

\s Returns a match where the string contains a white space 
character "\s"

\S Returns a match where the string DOES NOT contain a white space 
character "\S"

\w Returns a match where the string contains any 
word characters (characters from a to Z, digits from 0-9, and 
the underscore _ character) "\w"

\W Returns a match where the string DOES NOT contain any word 
characters "\W"

\Z Returns a match if the specified characters are at the end of 
the string "Spain\Z"
"""

"""
Sets:
Enclosed in [ ]
Set Description:

[arn] Returns a match where one of the specified characters (a, r, 
or n) are present

[a-n] Returns a match for any lower case character, alphabetically 
between a and n

[^arn] Returns a match for any character EXCEPT a, r, and n

[0123] Returns a match where any of the specified digits 
(0, 1, 2, or 3) are present

[0-9] Returns a match for any digit between 0 and 9

[0-5][0-9] Returns a match for any two-digit numbers from 00 and 59

[a-zA-Z] Returns a match for any character alphabetically between a 
and z, lower case OR upper case

[+] In sets, +, *, ., |, (), $,{} has no special meaning, so [+] 
means: return a match for any + character in the string
"""

"""
Regex Functions:
- Findall
- Search
- Split 
- Sub
"""
#Search
#Search searches for a string with or without metacharacters

#import RegEx class
import re

#string text
txt = "ID1008, John Doe, Texas" 

#obj x = regEx search fx()
#x = re.search("Florida", txt)
#if x == None:
#    print("Not Found")    
    
x = re.search("Texas", txt)
if x != None:
    #start fx returns the position that Texas starts at in the string    
    print(x.start())
else:
    print("Not Found")    
    
"""
Search
Search returns a match object if a a match is found and None if it 
isnt
"""
txt = "ID1008, John Doe, Texas" 
x = re.search("^ID.*Texas$", txt)
print(x) # prints: <re.Match object; span=(0, 23), match='ID1008, John Doe, Texas'>

x = re.search("Texas", txt)
print(x) # prints: <re.Match object; span=(18, 23), match='Texas'>