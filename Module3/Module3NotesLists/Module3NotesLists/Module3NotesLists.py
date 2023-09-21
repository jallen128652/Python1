#*************************Lists***************************
#List creation
#Lists can be created with square brackets []
#a list is a collection which is ordered and changeable
#myList1 = ["Joe", "Cindy", "Bill", "Sandra"]
#myList2 = [6, 7, 3, 1]
#myList3 = [] #creates an empty list
#Accessing and changing the list
myList = ["Joe", "Cindy", "Bill", "Sandra"]
myList[2] = "Frank" #Changes Bill to Frank
print(myList)
print(myList[2])

#Accessing and changing the list with numeric values
myList = [5, 9, 4, 7]
print(myList)
myList[2] = myList[3] + 1 #changes the 4 to a 7 and adds 1 to make it 8
print(myList)

#Adding an item to the end of a list(append)
myList = ["Joe", "Cindy", "Bill", "Sandra"]
print(myList)
myList.append("Hazel") # adds hazel to the end of the list or index 4
print(myList)

#insert items to a list at an index position
myList = ["Joe", "Cindy", "Bill", "Sandra"]
print(myList)
myList.insert(2, "George") #inserts George at index position 2. 2 arg fx
print(myList)
#note George pushes Bill and Sandra to the right an index position

#Deleting and item at an index
myList = [7, 14, 1, 0]
print(myList)
del myList[3] #deletes the 0
print(myList)
#note it deletes the index position as well instead of leaving a null value

#Deleting an entire list
#Deleting the whole list deletes the entire var from the mem location
myList = [7, 14, 1, 0]
print(myList)
del myList
#print(myList) #throws a syntax error

#Clearing a list
myList = [7, 14, 1, 0]
print(myList)
myList.clear() #clears the vals and index positions leaving just an empty list
print(myList)

#Determining the lenght of a list with len() fx
myList = [7, 14, 1, 0]
print(len(myList)) # prints 4

if len(myList) > 0:
    print("myList isn't empty")
else:
    print("myList is empty")
    
#Practice exercise
myList = []
inNum = int(input("Enter an integer or -1 to quit: "))
while inNum != -1:
    myList.append(inNum)
    inNum = int(input("Enter another integer or -1 to quit: "))
print(myList)
 