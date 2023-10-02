#*****************************Functions cont...**************************
#Multiple paramaters
#example
def printSquare(num):
    print(str(num) + " squared is " + str(num * num))
    
def printAdd(num1, num2):
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    
printSquare(5)
printAdd(6, 4) #must have the same number of values as args passed to the fx

#Arguments must be passed to the function in order
#If a function has multiple parameters you must pass the same number of
# arguments

#Default Parameters

#You can get past incomplete number of parameters by specifying default
# parameter values
# If the parameter is missing, the default value is used
#example
def printAdd(num1, num2 = 2):
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    
printAdd(6)
printAdd(5, 5) #note when you pass in vals it overrides the default values

#Keyword parameters

#You can send data to a function in key = value pairs.
#This way, the order of parameters can be ignored.

def printName(fName, lName):
    print(fName + " " + lName)
    
printName(lName = "Lozano", fName = "Tony") 
#note you are assigning vals as you pass args

#Parameter types

#You can send other data types and objects to functions. Lists, dictionaries,
# etc.`
#example
def printNames(names):
    for x in names:
        print(x)
        
n = ("Tony", "Bob", "Jill")
printNames(n) #passes in the tuple

#example2
def addName():
    sName = input("Enter a name: ") #inputs the name from user
    fname.append(sName) #appends to the list
    
fname = ["Bill", "Tony", "Bill"] #the list **note fname can be accessed by 
# the fx because fname is at the module level**
addName() #calls the fx
print(fname) #prints updated list

#alt method passing in the list
def addName(n): # n is reference to fname because the call associated them
    sname = input("Enter a name: ")
    n.append(sname)
    
fname = ["Bill", "Tony", "Bill"]
addName(fname)
print(fname)
