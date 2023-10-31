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
