#***********************Lists part 2************************
#Looping
#For loop list looping
days = ["Monday", "Wednesday", "Friday"]
for x in days:
    print(x)
    
#List looping by index
days = ["Monday", "Wednesday", "Friday"]
for x in range(1, 2): #Last number not included #range(start index, end index)
    print(days[x])
    
#alt
days = ["Monday", "Wednesday", "Friday"]
for x in range(0, len(days)): #last number not inclusive so it won't go out of range
    print(days[x])
    
#While loop
days = ["Monday", "Wednesday", "Friday"]
numItems = len(days)
loopControl = 0
while loopControl < numItems:
    print(days[loopControl])
    loopControl += 1
#for loop is always best for lists

#Sorting a list ascending
myList = ["Joe", "Cindy", "Bill", "Sandra"]
print(myList)
myList.sort()
print(myList)

#Sorting a list descending
myList = ["Joe", "Cindy", "Bill", "Sandra"]
print(myList)
myList.sort(reverse = True)
print(myList)

#Search a list and append to a new list based on search criteria
myList = ["Joe", "Cindy", "Bill", "Sandra"]
newList = []

for x in myList: #loops through myList
    if "i" in x: #searches for words with "i"
        newList.append(x) #appends those words to newList
        
print(newList)

#alt
#syntax  newList = [exprssion for item in iterable if condition == True]
myList = ["Joe", "Cindy", "Bill", "Sandra"]
newList = [x for x in myList if x != "Joe"] #basically a loop and if inside a list
print(newList) #prints ['Cindy', 'Bill', 'Sandra']

#Deep copying a list
"""
You cannot copy a list simply by typing:
list2 = list1

list2 will only be a reference to list1. They point to the same memory,
changing 1 will change both.
"""
#to make a separate copy and ensure the original is unchanged
myList = ["Joe", "Cindy", "Bill", "Sandra"]
myListCopy = myList.copy()

print(myListCopy)

#alt
myList = ["Joe", "Cindy", "Bill", "Sandra"]
myListCopy = list(myList) #python list() fx

print(myListCopy)

#Joining lists similar to concatenation
myList1 = ["Joe", "Cindy", "Bill", "Sandra"]
myList2 = ["Abby", "Doug", "Will", "Tony"]

myList3 = myList1 + myList2

print(myList3)

"""
List Methods
Python has a set of built-in methods that you can use on lists.

Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
