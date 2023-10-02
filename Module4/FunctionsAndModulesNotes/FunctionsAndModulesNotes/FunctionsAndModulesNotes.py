#*************************Functions Notes*************************
"""
What are functions and modules?

Function - A block of code that runs when called. You can pass data, and get
data from functions.

Module - A file of functions you can include in your program

Functions and Modules provide modularity to your program

Creating Python Functions
Functions are created with def keyword (short for define)
"""
#def functionName():
#	function block 

#functions need to be defined before they are called or above where they
# are called.
#example menu fx

def printMenu():
    print("-------- Menu --------\n")
    print("1. View List")
    print("2. Add Entry")
    print("3. Find Entry")
    print("4. Delete Entry")
    print("5. Quit")
    
#call the fx
#printMenu()

"""
Simple Parameters

Functions can have parameters.
You can pass Arguments (data) to a functions parameters
Parameters are placed in the function definition between the parenthesis
You can have as many parameters as you need, separate them with commas.
"""
#example

#define the fx
def printSquare(num):
    #do calculations with the fx
    print(str(num) + " squared is " + str(num * num))

#call the fx and pass args    
#printSquare(7)
#printSquare(3.14)

"""
Scope

Python variables are scoped to the innermost function, class, or module in 
which they're assigned.
"""
#example
def test():
    a = 10
    
#test() # the call works
#print(a) #this print statement doesn't as it's outside of scope
#basically print call doesn't have access to a outside of the test fx

"""
Python mimics by value parameter passing

If a function changes a value of a parameter, it is
local and doesn't reflect back to the calling
procedure

The mechanics behind the scene arent exactly
byval, but they have the same effect
"""
#example
# defien fx and pass var name
def printName(name):
    #assign value to var inside fx
    name = "Bill"
    #print var
    print(name)
# assign value to new var    
n = "Tony"
#print that var
print(n)
#pass that var in so that the fx uses it inplace of the local var
printName(n)
#print the var again --- no change as the value only changed inside the fx
print(n)

#practical exercise
#user input
num1 = int(input("Enter an integer and see if it's even or odd: "))

#define fx with var
def evenOrOdd(num1):
    #inner fx calcs
    if num1 % 2 == 0:
        print(str(num1) + " is an even number.")
    else:
        print(str(num1) + " is an odd number.")
#call fx pass in user input var        
evenOrOdd(num1)
    