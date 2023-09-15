#*******************Notes Module2*********************
#Python Comparison Operators
#Comparison operators are used to compare two values:

#Operator			Name						Example	
#==					Equal						x == y	
#!=					Not equal					x != y	
#>					Greater than				x > y	
#<					Less than					x < y	
#>=					Greater than or equal to	x >= y	
#<=					Less than or equal to		x <= y

#Python Logical Operators
#Logical operators are used to combine conditional statements:

#Operator	Description									Example	
#and 	Returns True if both statements are true		x < 5 and  x < 10	
#or		Returns True if one of the statements is true	x < 5 or x < 4	
#not	Reverse the result, returns False if true		(x < 5 and x < 10)
"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""
#Example
#If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#Indentation
#Python relies on indentation (whitespace at the beginning of a line) to 
# define scope in the code. Other programming languages often use
# curly-brackets for this purpose.
"""
Example
If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
"""

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
#Else
#The else keyword catches anything which isn't caught by the preceding
# conditions.
#Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#You can also have an else without the elif

#Short Hand If
#If you have only one statement to execute, you can put it on the same
# line as the if statement.
#Example
#One line if statement:

if a > b: print("a is greater than b")

#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else,
# you can put it all on the same line:
#Example
#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

#You can also have multiple else statements on the same line:
#Example
#One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#**********And***********
#The and keyword is a logical operator, and is used to combine conditional
# statements:
#Example
#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
#*********Or**************
#The or keyword is a logical operator, and is used to combine conditional
# statements:
#Example
#Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#*************Not***************
#The not keyword is a logical operator, and is used to reverse the result
# of the conditional statement:
#Example
#Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
#************Nested If************
#You can have if statements inside if statements, this is called nested if
# statements.
#Example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
#***********The pass Statement*********
#if statements cannot be empty, but if you for some reason have an if
# statement with no content, put in the pass statement to avoid getting an
#  error.
#Example
a = 33
b = 200

if b > a:
  pass

#************Indentation****************
"""
Python Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

ExampleGet your own Python Server
if 5 > 2:
  print("Five is greater than two!")
Python will give you an error if you skip the indentation:

Example
Syntax Error:

if 5 > 2:
print("Five is greater than two!")
The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

Example
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

Example
Syntax Error:

if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""
#ex1
#Simple if
num1 = int(input("Enter a number greater than 100: "))

if num1 > 100:
  print("The number is greater than 100")
  num2 = num1 + 50 #num2 is not local to just this block see the next print
  
print(num2)

#ex2
#Multiple elses with elif
grade = input("Enter a letter grade: ")
grade = grade.upper() #convert to upper and store in grade var

if grade == "A":
  print("The GPA is 4.0")
elif grade == "B":
  print("The GPA is 3.0")
elif grade == "C":
  print("The GPA is 2.0")
elif grade == "D":
  print("The GPA is 1.0")
elif grade == "F":
  print("The GPA is 0.0")
else:
  print("The letter you entered is not valid.")
  
#ex3
#Nested if statements
grossPay = 0.0
hoursWorked = int(input("Enter hours worked: "))
payRate = float(input("Enter hourly pay rate: "))
hourlyEmployee = input("Is the employee hourly? (y/n): ")
hourlyEmployee = hourlyEmployee.upper()
if hoursWorked > 40:
    if hourlyEmployee == "Y":
      basePay = 40 * payRate
      overTime = (hoursWorked - 40) * payRate
      grossPay = basePay + overTime
    else:
      grossPay = hoursWorked * payRate
else:
  grossPay = hoursWorked * payRate
  
#****************Range testing***************
"""
if you want to test a var against a range, python has a special syntax you
can use.
"""
#consider the standard method of checking range:
#   is the number between 1 and 100?
number = int(input("Enter a number between 1 and 100: "))

if number >= 1 and number <= 100:
  print("In range.")
else:
  print("Not in range.")
  
#python special range syntax method:
number = int(input("Enter a number between 1 and 100: "))

if (1 <= number <= 100):
  print("In range.")
else:
  print("Not in range.")
  
#Practice exercise:
length = int(input("Enter the lenght of a rectangle: "))
width =  int(input("Enter the width of a rectangle: "))   

if length == width:
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")
    if length > width:
      print("The length of the rectangle is longer.")
    else:
      print("The width of the rectangle is longer.")
      
#*********************Loops*************************
#******************while loop*****************
#syntax:
"""
#loop control var
num1 = 1
while condition:
    #indented code line or block
    print("inside loop")
    #update loop control var
    num1 += 1
    
#outside the loop after exit
print("after loop")    

While loops can be sentinel controlled or counter controlled
sentinel controlled stops when the condition detects certain values
counter controlled repeats based on a counter

sentinel values are values that trigger loop entry or exit

"""
#example sentinel controlled while loop
inputValue = int(input("Enter a number or -999 to exit: "))

while inputValue != -999:
  print("Loop body executed.")
  inputValue = int(input("Enter another number or -999 to exit: ")) 
  
print("You have exited the loop.")

#example2 with range
inputValue = int(input("Enter a number between 1 and 100: "))

while inputValue < 1 or inputValue > 100:
  print("Number not in range.")
  inputValue = int(input("Enter another number between 1 and 100: ")) 
  
print("You have exited the loop.")

#example counter controlled while loop
#counter var
num1 = 1
while num1 <= 5:
  print(num1)
  num1 += 1
  
print(str(num1) + " is the final count")

# counter controlled while loop with accumulator
c = 1
total = 0
newVal = 0
while c <=5:
  newVal = int(input("Enter number " + str(c) + ": "))
  total = total + newVal #accumulation
  c += 1 #loop counter
  
print("The total is: " + str(total))

#*********************for loops**********************
"""
Python for loops are used for iterating through a sequence, range, or
other iterable object.

A common sequnce structure is a python list

A python list is a list of items stored in one var.

#declaration of list days
days = ["Monday", "Tuseday", "Wednesday", "Thursday", "Friday"]

We will discuss lists more in depth in later units. Just remember they 
are a list of items in one var.
"""


      

  
