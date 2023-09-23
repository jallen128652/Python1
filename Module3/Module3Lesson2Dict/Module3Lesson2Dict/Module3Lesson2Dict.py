#**********************Dictionary Notes********************
"""
Dictionary is a collection which is changeable and indexed. No duplicate items.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, 
dictionaries are unordered. Dictionaries store key:value pairs.
"""
record = {"fname": "Tony",
          "lname": "Lozano",
         "age": 21} #note it can mix datatypes
print(record)

#Accessing Items
print(record["lname"]) #the subscript is the key value

#Accessing Items with get and assigning them to a var
x = record.get("lname")
print(x)

#Getting the stored keys
x = record.keys()
print(x)
# prints dict_keys(['fname', 'lname', 'aga'])

#Two ways to change values
record["fname"] = "Anthony" #uses key subscript and assigns new val
record.update({"age": 30}) #uses update() fx with full key: value pair in {}
print(record)

#Two ways to add keys/values
record["weight"] = 180 #uses key subscript and assigns new val
record.update({"phone": "555-555-1234"}) #uses update() fx with full key: value pair in {}
print(record)

#Removing items using pop() fx
record.pop("age") #uses key to remove key: value pair
print(record)

#Removing items using popitem() fx
record.popitem() #removes the last inserted item "phone"
print(record)

#Looping through Dicts
for x in record:
    print(x) #prints keys vertically
    
for x in record:
    print(record[x]) #prints values vertically
    
#item method looping(key: value pairs)
for x, y in record.items():
    print(x, y)    
#prints:
#fname Anthony
#lname Lozano
#weight 180

#Copying a Dictionary
#Like with lists, assigning a dictionary to a different variable is only a
# shallow copy (a reference).
#Use the copy method to create a separate copy
recordCopy = record.copy()
print(recordCopy)
#this allows you to modify a copy while not changing the original

#Dictionary Methods
"""
Python has a set of built-in methods that you can use on dictionaries.

Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""

#practical exercise
#What if statement would make this program work?
record = {
    "user1":"abcd", 
    "user2":"password",
    "user3":"opensesame"}
user = input("enter username: ")
password = input("enter password: ")
if (user == record["user1"] and password == record["user2"]):
    print("access granted!")
else:
   print("access denied!")  

#zip() fx   
#another way to create pairs using tuples
#The zip function will take 2 tuples, and combine them pairwise (dropping extras)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b) #combines the two tuples
#use the tuple() fx to display a readable version of the result:
print(tuple(x))
#prints: (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))