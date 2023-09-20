#***********************Module3 Notes********************
#Python lists
# 4 built in container classes: lists, tuples, sets, dictionary
# the stored data can be strings, ints floats or any other object
# python allows items in a collection to be of mixed data types
"""
collections can be ordered or unordered
-ordered collections each item has a position and can normally be indexed
-unordered collections you don't know how items are stored in the collection
"""
# python doesn't have built in arrays
"""
a list is a collection which is ordered and changeable
a tuple is a collection which is ordered and unchangeable Basically read only
a set is a collection which is unordered and unindexed. No duplicate items
a dictionary is a collection which is unordered, changeable and indexed. No duplicate items 
"""
#Lists can be created with square brackets []
#a list is a collection which is ordered and changeable
myList1 = ["Joe", "Cindy", "Bill", "Sandra"]
myList2 = [6, 7, 3, 1]
myList3 = [] #creates an empty list

#Tuples are created with round brackets ()
#a tuple is a collection which is ordered and unchangeable Basically read only
myTuple1 = ("Joe", "Cindy", "Bill", "Sandra")
myTuple2 = (6, 7, 3, 1)

#Indexes
"""
Each item in a list has an index
The index refers to the items position in the list
Indexes give you a reliable way to access individual items
Index always starts with zero
"""
#Index:		0		1		2		 3		  4 	  5
myList = ["Joe", "Cindy", "Bill", "Sandra", "Gary", "Sam"]
print(myList[1]) #prints Cindy

#Negative Indexes
"""
While python supports negative indexes, most other commercial langs do not.
Ruby and Lua are the only other exceptions
We won't be using negative indexes in the labs for this course
"""
#Index:		-6		-5		-4		 -3		  -2 	  -1
myList = ["Joe", "Cindy", "Bill", "Sandra", "Gary", "Sam"]
print(myList[-3]) #prints Sandy

#Sets are created with curly brackets {}
#a set is a collection which is unordered and unindexed. No duplicate items
#sets have special purpose that we will see later on
setA = {2, 3, 4, 7, 8}
setB = {"Joe", "Cindy", "Bill", "Sandra", "Gary", "Sam"}

#Dictionaries store key:value pairs
#a dictionary is a collection which is unordered, changeable and indexed. No duplicate items
record = {"fname": "Tony", "lname": "Lozano", "age": 21}