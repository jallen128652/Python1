# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: Numbers
# Description: Asks the user to enter 10 odd numbers and prints the largest,
# smallest and average of all numbers
# Note: Remember to save often and commit to git once tested

#Instructions: Write a program that accepts from the user 10 odd numbers in
# the range of 1 - 99 and adds them to a list. These are all numbers whose
# value % 2 == 1.   If the number is even, ask the user to enter another
# number, at the end you should have 10 odd numbers.  Write out the following
# numbers to a file: 
#  On-screen printout with descriptions. 
#	The largest number
#	The smallest number
#	The average of the numbers.

numbers = [] # list to store the numbers
#promps and greetings
print("Welcome to the odd numbers program!\n")
choice = input("Would you like to enter 10 odd numbers? (Y/N): ")
# while loop so user can use this program as many times as they want
while (choice.upper() == "Y"):
    #loops 10 times for 10 input numbers
    min1 = 0 #loop control var
    while min1 < 10:        
        num = int(input("Please enter an odd number: "))
        # validates the number is odd or re-prompts the user
        if (num % 2) == 1:
            numbers.append(num)
            min1 += 1
        else:
             print("That number was even! ")             
    #prints the user inputs
    print("\nYou entered the following numbers: ")
    print(numbers[0:])
    print("\n")
    #vars for calculations
    small = 99999999999999999 #initialize high
    large = 0 # initialize low
    total = 0 # initialize
    #loops through the list and finds the smallest, largest and adds up the total
    for x in range(0, len(numbers)):
        if numbers[x] < small:
            small = numbers[x]
        elif numbers[x] > large:
            large = numbers[x]
        total += numbers[x]
     
    #Calculates avg    
    average = total / 10
    #open and write to file
    file = open("output.txt", "w")
    file.write("The smallest number is: " + str(small) + "\n")
    file.write("The largest number is: " + str(large) + "\n")
    file.write("The average of the numbers is: " + str(average) + "\n")
    file.close()
    #print from the file
    file = open("output.txt", "r")
    for x in file:
        print(x)
    file.close()
    #clears the list so the total doesn't continue to accumulate
    numbers.clear()
    #loop control var update
    choice = input("\nWould you like to enter another 10 odd numbers? (Y/N): ")
    
             
             

