#******************************Sets Notes********************

#A set is a collection which is unordered, unchangeable*, and unindexed.
#Use curly braces for sets.
#Sets don’t allow duplicates

setA = {2,3,4,7,8}
setB = {"Joe", "Cindy", "Bill", "Sandra", "Gary", "Sam"}
print(setB) 

#Sets are used for group operations, things like Union, Difference and
# Intersection(shared or overlap)
#Union finds all things in both sets
#Intersection finds things both sets have in common
#Difference finds things that are different in each set

#Accessing
#You can't access items by referring to indexes
#You can use for… in. Pay attention to order.
mySet = {"Joe", "Cindy", "Bill", "Sandy"}

for x in mySet:
    print(x)
# prints vertical list in different order each time because sets are unordered

#Accessing
#You can check if an item is in a set. 
mySet = {"Joe", "Cindy", "Bill", "Sandy"}
print("Bill" in mySet) # returns a bool value

if ("Bill" in mySet): # if true print Yes
    print("Yes")
    
#Adding to a set
mySet = {"Joe", "Cindy", "Bill", "Sandy"}

mySet.add("Mike") #add() fx
print(mySet)

#Adding one set to another set
mySet1 = {"Joe", "Cindy", "Bill", "Sandy"}
mySet2 = {"Abby", "James", "Mary", "Zeke"}
mySet1.update(mySet2) #update() fx
print(mySet1)

#Removing an item form a set
#If the item isnt in the list, remove will error
mySet = {"Joe", "Cindy", "Bill", "Sandy"}
mySet.remove("Bill") #remove() fx
print(mySet)

#alt discard() fx
#If the item isnt in the list, discard will not error
mySet = {"Joe", "Cindy", "Sandy"}
mySet.discard("Bill") #discard() fx
print(mySet)

#alt pop() fx
#Pop removes an item that you can assign to a variable.
#You don’t know what item will be removed, and it could be different every time
mySet = {"Joe", "Cindy", "Bill", "Sandy"}
print(mySet)
x = mySet.pop() #removes a random item and assigns it to the var
print(x)
print(mySet)

#*********The purpose for sets are the following methods***********
#Union
#Union creates a new set that is the combination of the 2 other sets.
#Notice duplicates are removed
mySet1 = {"Joe", "Cindy", "Bill", "Sandy"}
mySet2 = {"Abby", "James", "Mary", "Bill"}
mySet3 = mySet1.union(mySet2)
print(mySet3) #The duplicate Bill was removed

#Difference
#This difference returns the items in mySet1 that aren't in mySet2
mySet1 = {"Joe", "Cindy", "Bill", "Sandy"}
mySet2 = {"Abby", "James", "Mary", "Bill"}
mySet3 = mySet1.difference(mySet2)
print(mySet3) # prints only the items that are unique to mySet1 'Joe', 'Cindy', 'Sandy'
#note it doesn't print the unique items in mySet2

#Intersection
#Intersection returns the items they have in common
mySet1 = {"Joe", "Cindy", "Bill", "Sandy"}
mySet2 = {"Abby", "James", "Mary", "Bill"}
mySet3 = mySet1.intersection(mySet2)
print(mySet3) #prints 'Bill' which is the only common item between the two sets

"""
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	                    Description
add()	                    Adds an element to the set
clear()	                    Removes all the elements from the set
copy()	                    Returns a copy of the set
difference()	            Returns a set containing the difference between two or more sets
difference_update()	        Removes the items in this set that are also included in another, specified set
discard()	                Remove the specified item
intersection()	            Returns a set, that is the intersection of two other sets
intersection_update()	    Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	            Returns whether two sets have a intersection or not
issubset()	                Returns whether another set contains this set or not
issuperset()	            Returns whether this set contains another set or not
pop()	                    Removes an element from the set
remove()	                Removes the specified element
symmetric_difference()	    Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                    Return a set containing the union of sets
update()	                Update the set with the union of this set and others
"""
#practical exercise
#Write the lines of code that shows the items in mySet2 that are not in mySet1.
mySet1 = {"Joe", "Cindy", "Bill", "Sandy"}
mySet2 = {"Abby", "James", "Mary", "Bill"}
mySet3 = mySet2.difference(mySet1)
print(mySet3) # prints only the items that are unique to mySet2
