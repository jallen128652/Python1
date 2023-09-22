#******************Tuples Notes****************
"""
Tuple is a collection which is ordered and unchangeable.
Tuples are created with parenthesis ()
"""
myTuple = ("Joe", "Cindy", "Bill", "Sandra")
myTuple = (6, 7, 3, 1)
#Most of the operations that delete or add items to tuples wont work.
myTuple = (6, 7, 3, 1)
#myTuple[2] = 7 #will cause an error
#Like lists , you can loop through tuples, print their values, etc
print(myTuple[2])
#Tuples are constant
#You can print a range of elements
myTuple = ("Joe", "Cindy", "Bill", "Sandra")
print(myTuple[2:3]) #Similar to string slicing. note it also prints the comma

#Updating Tuples
#convert to list, change, convert back to tuple
"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable,
or immutable.As a workaround you can temporarily convert it to a list. This will
allow you to add or change items.
"""
myTuple = ("Joe", "Cindy", "Bill", "Sandra")
myList = list(myTuple) #list constructor
myList.append("Mike")
myTuple = tuple(myList) #Tuple constructor

print(myTuple)
#You can however combine tuples
myTuple = ("Joe", "Cindy", "Bill", "Sandra")

temp = ("Mike",) #needs a comma

myTuple += temp

print(myTuple)
#When creating a tuple with only one item, remember to include a comma after the
# item, otherwise it will not be identified as a tuple.

#Unpacking Tuples
#In python you can extract tuple values back into variables
myTuple = ("Joe", "Cindy", "Bill", "Sandra")
(first, second, third, fourth) = myTuple

print(second)
#The number of variables must match the length of the tuple

#Tuples have 2 built in methods
#count() – returns the number of times the value appears in tuple
M = (1,5,8,3,5,2)
n = M.count(5) # returns 2
print(n)

#index() – finds first occurrence of the specified value
myTuple = ("Joe","Cindy","Bill","Sandra")
print (myTuple.index("Cindy")) # prints 1

#practice exercise
states = ("Nevada", "Texas", "California", "Oregon")
myState = input("Please enter a state: ")
num = states.count(myState)
if num == 0:
    print(myState + " was not found.")
else:
    print(myState + " was found.")