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
#tabby = Cat()
#assigns values to the objects properties
#tabby.name = "Garfield"
#tabby.color = "Orange"
#tabby.weight = 5.3
#calls the objects class fx
#tabby.purr()
    
"""
Object methods
Object Methods functions that belong to an object. Below eat and purr are object methods
"""
"""
class Cat:
    #properties or variables
    name = ""
    color = ""
    weight = 0.0
    food = "Cat Food"
    isHungry = True
    #methods or fx's
    def eat(self):
        #note the properties have self assigned to it inside the class   
        if self.name == "Garfield":
            food = "Lasagna"
        print(self.name + " eats " + food)
        self.purr()
        isHungry = False      
        
    def purr(self):
        print("Puuuuuurrrrrr...")
"""        
"""
The self keyword
The self keyword is how a class instance refers to itself.
Every class function has at least one parameter that is the self keyword.
Variables are referenced by using: self.variableName
It needs to be included in the definition of class functions or the following error is given.
"""
        
#example instantiation and use of the Cat() class
"""
tabby = Cat()
tabby.name = "Garfield"
tabby.color = "Orange"
weight = 5.3
tabby.eat()
"""

"""
Modifying properties
In the last example notice how we changed some of the variables from outside the class
While this is ok, normally with classes, you want to let the methods change parameters
"""

"""
__init__() function ***note 2 underscores before and after the init***

The __init__() function is a dunder function so named for the double underscore before and
after the name.
Python classes have several dunder functions that are created automatically if you don't
override them.
Overriding a function is creating your own version to override the default version.
__init__() function is called automatically whenever a new object is created from a class.

"""

from tempfile import NamedTemporaryFile


class Cat:
    #properties or variables
    name = ""
    color = ""
    weight = 0.0
    food = "Cat Food"
    isHungry = True
    #methods or fx's
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def eat(self):
        #note the properties have self assigned to it inside the class   
        if self.name == "Garfield":
            food = "Lasagna"
        print(self.name + " eats " + food)
        self.purr()
        isHungry = False      
        
    def purr(self):
        print("Puuuuuurrrrrr...")
# When creating an instance of cat, you can pass parameters to the class        
tabby = Cat("Garfield", "Orange", 5.3)
tabby.eat()            

#example
class Employee:
    ID = ""
    lastName = ""
    firstName = ""
    payRate = 0.0
    hoursWorked = 0
    def __init__(self, eid, fname, lname):
        self.ID = eid
        self.lastName = lname
        self.firstName = fname
    def setPayRate(self, rate):
        self.payRate = rate
    def setHoursWorked(self, hworked):
        self.hoursWorked = hworked
    def calcGrossPay(self):
        if self.hoursWorked > 40:
            basePay = 40 * self.payRate
            overTime = (self.hoursWorked - 40) * (self.payRate * 1.5)
            grossPay = basePay + overTime
        else:
            grossPay = self.hoursWorked * self.payRate
        return grossPay
    
#example instantiation and call to the class
emp1 = Employee("1001", "John", "Smith")
emp1.setPayRate(15.00)
emp1.setHoursWorked(45)
print(emp1.calcGrossPay())

"""
Declaring properties
You arent required to declare your properties before you use them in Python
"""
class Dog:
    # When deleting properties, be careful of default values like name below
    name = "Fido"
    def __init__(self, n):
        self.name = n
    def printName(self):
        print(self.name)
        
#myDog = Dog("Rex")
#myDog.printName()
#myDog.printName()
 
"""
Deleting properties
You can delete properties
"""
#myDog = Dog("Rex")
#myDog.printName()
#del myDog.name
#myDog.printName() 

# note we deleted myDog.name, but there was a default property name that printed Fido 
# without the default property it would have thrown a syntax error for print(self.name)  
# because it no longer existed for the second call. ***of note don't call a deleted property again***

"""
Deleting an entire object
Delete object when done to free memory
del objectName
"""
myDog = Dog("Rex")
myDog.printName()
del myDog

"""
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

Example
class Person:
  pass
"""  
