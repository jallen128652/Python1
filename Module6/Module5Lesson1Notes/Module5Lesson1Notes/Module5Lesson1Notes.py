#************************Exception Handling Notes******************
"""
Exceptions versus Syntax Errors:
There are (at least) two distinguishable kinds of errors: syntax errors and exceptions. Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint
you get while you are still learning Python:
"""
#example syntax error:
"""
while True
	print('Hello world')
"""
# it's missing the : after True causing a syntax error

"""
Even if a statement or expression is syntactically correct, it may 
cause an error when an attempt is made to execute it.
Errors detected during execution are called exceptions and are not
unconditionally fatal:
"""
#example exception
"""
print('Hello world' + 10)
"""
#we can't concat a str and int so it throws an exception

"""
Raise keyword:
As a Python developer you can choose to raise (or throw) an 
exception if a condition occurs.
"""
#examples of the raise keyword
"""
x = -1
if x < 0:
    raise Exception("Sorry, no number below zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
""" 
#both examples throw exceptions 

"""
Assert Keyword:
The assert keyword is used when debugging code.
"""

#x = 0
#if condition returns False, AssertionError is raised:
#assert x > 0, "x should be greater than 0"

