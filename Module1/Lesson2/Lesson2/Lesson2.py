#******************Variables section********************
#you don't declare and initialize variables in python
#a variable is initialized the moment you assign a value to it

#casting
x = str(3)	#x will be '3'
y = int(3)	#y will be 3
z = float(3)	#z will be 3.0
print(x)
print(y)
print(z)

#get the type of var
print(type(x))
print(type(y))
print(type(z))

#strings can be contained in '' or ""

#vars are case sensitive
a = 4
A = "Sally"
print(a)
print(A)

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
#I use camelCase

#multiple vars in one declaration
x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)

#one val to many vars
x = y = z = "strawberry"
print(x)
print(y)
print(z)

#Unpack a collection:
#If you have a collection of values in a list, tuple etc. 
#Python allows you to extract the values into variables. 
#This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#print is an output fx
#you can print multiple vars by separating them by a comma
x = "python"
y = "is"
z = "fun"
print(x, y, z) # similar results to concatenation except it adds a space

#concatenation print notice I added spaces after the first 2 vars 
x = "python "
y = "is "
z = "fun"
print(x + y + z)

#the + can also be a unary operator
x = 5
y = 10
print(x + y)
# note can't mix strings and numeric data types or syntax error occurs

#commas work best with multi var print concatenation
x = 5
y = "john"
print(x, y)

# Global vars
#Global variables can be used by everyone,
# both inside of functions and outside.
x = "awesome"

def myFunc():
    print("Python is " + x)

myFunc()

#If you create a variable with the same name inside a function,
# this variable will be local, and can only be used inside the
# function. The global variable with the same name will remain
# as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#you can override this by declaring the var using global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Also, use the global keyword if you want to change a global
# variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#**********************End of vars*****************************

#*********************DataTypes Section************************
#               **python is a class based lang**
# data types and examples:
"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""
# setting specific datatypes and examples
"""
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
"""
# Datatype definitions
# these classes mimic primitive datatypes
"""
int - integer is a whole number, negative or positive without decimals of 
unlimited length
float - floating point number, negative or positive with one or more decimals
bool - contains the vals of True or False(case sensitive)
string - a string of characters enclosed in single or double quotes;
***Like many other popular programming languages, strings in Python are arrays of
bytes representing unicode characters. However, Python does not have a character
data type, a single character is simply a string with a length of 1. Square
brackets can be used to access elements of the string.***
"""

#Datatype examples
#int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#string
print("Hello")
print('Hello')

#multiliine string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# accessing characters at a string position: remember indices start at 0
a = "Hello, World!"
print(a[1])
# looping through a string
for x in "banana":
  print(x)

#string length fx
a = "Hello, World!"
print(len(a))

#check string
#To check if a certain phrase or character is present in a string, we
# can use the keyword "in".
txt = "The best things in life are free!"
print("free" in txt)
#using an "if" statement 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#using the "not in" statement  
txt = "The best things in life are free!"
print("expensive" not in txt)

#string slicing
"""
You can return a range of characters by using the slice syntax. Specify the start
index and the end index, separated by a colon, to return a part of the string.
"""
#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5]) #prints: Hello
#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:]) #prints: llo, World!
#Use negative indexes to start the slice from the end of the string:
"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2])
