# example header comments for the assignment submission

# Author: Tony Lozano 
# Course: ITSE 1371
# Program Name: Example
# Description: An example for module 1



#setting up repo
print("Hello, world!")
print("testing 123")
#syntax print can only print strings
A = 100

print("This is a literal string")
print("Variable A contains an int: " + str(A))

#python is an indented lang
if(A < 100):
	print("A is less than " + str(A))
else:
	print("A is greater than or equal to " + str(A))
	
#Python doesn't have strongly typed variables	
A = "This is a string now"
print(A)