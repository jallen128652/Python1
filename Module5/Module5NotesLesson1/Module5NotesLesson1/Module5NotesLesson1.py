#***********************Classes and Inheritance notes************************
"""
What is a class?
A class is a reusable blueprint for a data type.
A class is a bundle of: 
- properties (variables and constants) 
- methods (functions)

What is an object?
In the real world a house is an instance of a blueprint
An object is an instance of a class.

From a class you can create an unlimited number of objects
Python is an object-oriented language

Semi-real world example class
Cat:
Cat's Properties
- Color 
- Weight 
- Hungry?
- Speed
Cats methods
- Purr() 
- Eat() 
- Run()

Why are classes useful?
Classes are reusable.
You can use a class to create self contained objects quickly
Later we will talk about inheritance, which allow you to extend a class to add functionality.

Syntax for Defining a Class
class ClassName:
# list of properties
# list of methods
"""
class Cat:
    #properties or variables
    name = ""
    color = ""
    weight = "" #in pounds
    isHungry = True
    #methods or fx's
    def purr(self):
        print("Puuuuuurrrrrr...")
        
"""
class Employee:
    #properties or variables
    ID = ""
    lastName = ""
    firstName = ""
    payRate = 0.0
    hoursWorked = 0
    #methods or fx's
    def calcGrossPay(self):
        grossPay = payRate * hoursWorked
        print("Gross Pay is: ${:,.2f}".format(grossPay)) 
"""
#Creating an instance of a class
#objectVar = className()

#instantiates(creates an instance of the class) the class or creates an object reference constructor
tabby = Cat()
#assigns values to the objects properties
tabby.name = "Garfield"
tabby.color = "Orange"
tabby.weight = 5.3
#calls the objects class fx
tabby.purr()
    
    

