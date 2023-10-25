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
        