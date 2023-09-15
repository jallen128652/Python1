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

For Syntax

for and in are keyword

each time the loop iterates, the variable is assigned the next item from the 
sequence.

#for loop syntax
for var in <sequence object>
    # loop body
"""
#example for loop iterating through a list
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for x in days:
  print(x + " morning")
  
#strings are also iterable objects
for letter in "Macguyver":
  print(letter)

#range function
"""
The range function makes the for loop a counting loop similar to c++/java for loops

the range() fx returns a sequence of numbers 
    *starting from 0 by default
    *and increments by 1(by default)
    *ends at a specified number
    
range(x) - with one parameter the range function returns the sequence 
from 0 to x-1.

range(10) - returns the sequence 0-9
"""
#example
for x in range(5): # x receives the next number in the sequence each iteration
  print(x) #convert if concatenating
"""
it prints:
0
1
2
3
4
"""
#range fx cont...
"""
You can also optionally specify a different starting value and encrement
range(start, end)

or 

range(start, end, increment) 
"""
#example range(start, end)
for x in range(2, 6):
  print(x)
  
"""
prints:
2
3
4
5
"""
#example range(start, end, increment)
for x in range(4, 12, 2):
  print(x)
  
"""
prints:
4
6
8
10
"""
#coding example using range and list with nested for loops
greek = ["alpha", "beta", "gamma"]

for letters in greek:
  for x in range(3):
    print(letters + " " + str(x))
    
"""
prints:
alpha 0
alpha 1
alpha 2
beta 0
beta 1
beta 2
gamma 0
gamma 1
gamma 2
"""
#coding exercise - for loop that prints multiples of 5 from 5 to 50
# remember it's x-1 for the end point
for x in range(5, 51, 5):
  print(x)
  