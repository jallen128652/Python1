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

"""
Try and except block:
The try except block, can be used to handle error that would 
normally crash a program.
"""
#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#The else block lets you execute code when there is no error.

#The finally block lets you execute code, regardless of the result 
#of the try- and except blocks.

"""
Exception Handling
When an error occurs, or exception as we call it, Python will 
normally stop and generate an error message.

These exceptions can be handled using the try statement:

Example:
The try block will generate an exception, because x is not defined:
"""
try:
  print(x)
except:
  print("An exception occurred")
"""
Since the try block raises an error, the except block will be 
executed.

Without the try block, the program will crash and raise an error:
"""
#Many Exceptions
#You can define as many exception blocks as you want, e.g. if you 
#want to execute a special block of code for a special kind of error

#Example
#Print one message if the try block raises a NameError and another 
#for other errors:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
"""
Else
You can use the else keyword to define a block of code to be 
executed if no errors were raised:
"""
#Example
#In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
"""
Finally
The finally block, if specified, will be executed regardless if the 
try block raises an error or not.
"""
#Example
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
#This can be useful to close objects and clean up resources:  
#Example
#Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
# the file doesn't exist so it prints the final except statement that's the same 
# indent as try  

"""
Built-in Exceptions
The table below shows built-in exceptions that are usually raised in Python:

Exception	            Description
ArithmeticError	        Raised when an error occurs in numeric calculations
AssertionError	        Raised when an assert statement fails
AttributeError	        Raised when attribute reference or assignment fails
Exception	            Base class for all exceptions
EOFError	            Raised when the input() method hits an "end of file" condition (EOF)
FloatingPointError	    Raised when a floating point calculation fails
GeneratorExit	        Raised when a generator is closed (with the close() method)
ImportError	            Raised when an imported module does not exist
IndentationError	    Raised when indentation is not correct
IndexError	            Raised when an index of a sequence does not exist
KeyError	            Raised when a key does not exist in a dictionary
KeyboardInterrupt	    Raised when the user presses Ctrl+c, Ctrl+z or Delete
LookupError	            Raised when errors raised cant be found
MemoryError	            Raised when a program runs out of memory
NameError	            Raised when a variable does not exist
NotImplementedError	    Raised when an abstract method requires an inherited class to override the method
OSError	                Raised when a system related operation causes an error
OverflowError	        Raised when the result of a numeric calculation is too large
ReferenceError	        Raised when a weak reference object does not exist
RuntimeError	        Raised when an error occurs that do not belong to any specific exceptions
StopIteration	        Raised when the next() method of an iterator has no further values
SyntaxError	            Raised when a syntax error occurs
TabError	            Raised when indentation consists of tabs or spaces
SystemError	            Raised when a system error occurs
SystemExit	            Raised when the sys.exit() function is called
TypeError	            Raised when two different types are combined
UnboundLocalError	    Raised when a local variable is referenced before assignment
UnicodeError	        Raised when a unicode problem occurs
UnicodeEncodeError	    Raised when a unicode encoding problem occurs
UnicodeDecodeError	    Raised when a unicode decoding problem occurs
UnicodeTranslateError	Raised when a unicode translation problem occurs
ValueError	            Raised when there is a wrong value in a specified data type
ZeroDivisionError	    Raised when the second operator in a division is zero
"""
