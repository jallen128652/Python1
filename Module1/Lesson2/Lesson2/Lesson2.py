#Variables section
#you don't declare and initialize variables in python
#a variable is initialized the moment you assign a value to it

#casting
import pprint


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