#*************************Modules Notes*************************
"""
What is a Module?

A module is simply a separate python file (.py) that can contain functions and
data (variables)Modules can be imported into your application.

You can use a module to create code libraries you can use in multiple applications

Adding a Python file

You can use any name for your module file.

The important thing to remember is the module py file has to be in the same
directory as your python app.

There are ways to import custom modules from directories, but we won't cover them
in this lesson.
"""
"""
Step1. in solution explorer right click on the project folder and click add

Step2. Select new item

Step3. Select Empty Module and modify the name

Step4. Click the add button
"""
#in main python file
#import the module using the below syntax:
# import fileName as alias(alias is optional, but reduces typing)
import myModule as mm
#calls the module.fx(arg, arg) and stores it in a var
iBigger = mm.larger(1, 2) #note w/out the alias you would type out the filename
#prints the var
print(iBigger)
#calls the module.var and prints
print(mm.pi)

#works with 2nd fx

hw = int(input("Enter Hours Worked: "))
pr = float(input("Enter Hourly Pay Rate: "))

GrossPay = mm.calculateGrossPay(hw, pr)

print("Gross Pay is ${:,.2f}".format(GrossPay))
