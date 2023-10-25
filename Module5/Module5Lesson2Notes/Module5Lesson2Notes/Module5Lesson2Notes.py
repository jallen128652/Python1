#*******************************Inheritance Notes***************************************
"""
Parent/Child:
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class also called base class is inherited by child classes.
Child class is the class that inherits from the parent class, also called derived class.
"""
#Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)

#instantiates class with new object x        
x = Person("Tony", "Lozano")
#calls class using object and executes fx
x.printname()

"""
Inherit from parent class:
The child class will inherit all methods and properties from the parent
class childClass(parentClass):
#new properties and methods
"""
#Child class
# the child class must name the parent class in parenthesis as seen on the next line
class Employee(Person):
    hoursWorked = 0
    payRate = 0.0
    def calcGrossPay(self, hours, prate):
        self.hoursWorked = hours
        self.payRate = prate
        if self.hoursWorked > 40:
            basePay = 40 * self.payRate
            overTime = (self.hoursWorked - 40) * (self.payRate * 1.5)
            grossPay = basePay + overTime
        else:
            grossPay = self.hoursWorked * self.payRate
        return grossPay
#instantiates class with new object x and passes vals    
x = Employee("Tony", "Lozano")
# calls parent class fx
x.printname()
# calls child class fx and passes vals
print(x.calcGrossPay(40, 15.00))

"""
Overriding the __init__() Function:

You can override the init, but if you only initialize new properties you will get errors
If you have an __init__ in the child class, the parent class version is not called
"""
#example override
#class Student(Person):
#    def __init__(self, fname, lname, id):
#        self.EmployeeID = id
        
#s = Student("Joe", "Smith", 1001)
#s.printname()
# Throws an error for the printname() in the Person class because the __init__ was overridden 

"""
The super function:
If you want to also call the parent init you can use the super function
"""
#example now with super()
"""
class Student(Person):
    def __init__(self, fname, lname, id):
        super().__init__(fname, lname)
        self.EmployeeID = id
        
s = Student("Joe", "Smith", 1001)
s.printname()
print(s.EmployeeID)
"""
# now we get the passed in vals and fx's from the superclass

"""
List of objects:
creating a list of objects and storing them
"""
#example
class Student(Person):
    def __init__(self, fname, lname, id):
        super().__init__(fname, lname)
        self.EmployeeID = id
# create list        
students = []
# instantiate objects and append to list
students.append(Student("Joe", "Smith", 1001))
students.append(Student("Tony", "Lozano", 1002))
#call function by object index
students[0].printname()
students[1].printname()

"""
Overiding Methods tip:
You can overide any method from the parent class, and the child class method will be used You can use super if you want to run both versions

You can creates classes in modules and import it into your main file to use that class
"""