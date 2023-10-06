# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BookStarter
# Description: This program manipulates the book.txt file and prints
# Note: Remember to save often and commit to git once tested
"""
Instructions:
The program should ask the user to enter a menu choice and perform that operation.
The view books option iterates through the lists and show the 9 book fields, one book per line.
Add a book to prompt the user to enter all 9 fields of book information. Append the data to the appropriate lists.
Find a book should search the lists on Book ID or Title, and display the book.
Delete a book, should delete the book from the lists.
Write book list to file should create an output.txt, and write all the records, comma-delimited to the file one book per line.
Quit should Exit the Program
Additional Requirements are to be performed after the steps above are completed.

Create a separate python module named helper.py
Place the function to display the menu in the helper.py file and call it from your menu system.
In helper.py create a function called isValidID(bID) that checks if the passed in book ID is exactly 4 characters. Return True if it is and False if it is not
In your Add Book Entry menu code, use the isValidID function to test the ID that the user entered. If it is not valid, have them repeat asking for a Valid ID.
Submit both BookStarter.py, and helper.py for grading.
"""
#import modules
import os

import Helper as h

#clear fx
clear = lambda: os.system('cls')

#create lists
sID = []
sTitle = []
sGenre = []
fPrice = []
sPaperback = []
iOnHand = []
sAuthorFirst = []
sAuthorLast = []
sPublisher = []

#open and read file
file1 = open("book.txt", "r")
#loop through file line by line
for sLine in file1:
    #separate and strip data
    record = sLine.strip().split(",")
    #store in lists
    sID.append(record[0].strip())
    sTitle.append(record[1].strip())
    sGenre.append(record[2].strip())
    fPrice.append(float(record[3].strip()))
    sPaperback.append(record[4].strip())  
    iOnHand.append(int(record[5].strip()))
    sAuthorFirst.append(record[6].strip())
    sAuthorLast.append(record[7].strip())
    sPublisher.append(record[8].strip())
#close file    
file1.close()    

#loop control val
go = "Y" #sentinal val
#loop until user is done
while (go.upper() == "Y"):
    #call menu fx from helper.py
    h.printMenu()
    #prompt for user input choice
    choice = int(input("\nEnter a menu option number: "))
    # option1 iterate through list with one book per line
    if choice == 1: 
        #clear menu
        clear()
        print("--------View Books Entry--------\n")
        #loop through lists[x]
        for x in range(len(sID)):
            #print lists line by line
            print(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                  str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                 str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                sAuthorLast[x] + ", " + sPublisher[x])
        #return to menu    
        junk = input("\nPress Enter to return to the menu.")    
    # option2 take inputs and append list and file
    elif choice == 2:
        clear()
        print("--------Add Book Entry--------\n")
        bID = str(input("Please enter the 4 digit book ID: ")) 
        #call fx in helper.py to validate the book id and loop till correct
        while h.isValidID(bID) == False:                   
            if h.isValidID(bID) == False:
                print("Invalid ID entry.")
                bID = str(input("Please enter the 4 digit book ID: "))
        #recieve the rest of the inputs and store to vars        
        bTitle = input("Please enter the book title: ")
        bGenre = input("FIC = fiction, PSY = Psychology, SFI = SciFi, MYS = Mystery, HOR = Horror\nCMP = Computers, ART = Art, PHI = Philosophy, POE = Poetry, TRA = Travel\nPlease enter the book genre 3 letter code: ")
        bPrice = float(input("Please enter the book price: $"))
        bPaperback = input("Paperback? (Y/N): ")
        bOnHand = int(input("How many currently on hand? "))
        aFname = input("Please enter the authors first name: ")
        aLname = input("Please enter the authors last name: ")
        bPublisher = input("Please enter the publishers name: ")
        #print and validate the entry
        print("\nYou entered: " + bID + " " + bTitle + " " + 
              bGenre + " " + "${:,.2f}".format(bPrice) + " " + bPaperback + " " +
              str(bOnHand) + " " + aFname + " " + aLname + " " +
              bPublisher)
        choice2 = input("\nSave this entry? (Y/N): ")
        #store the entry
        if choice2.upper() == "Y":
            sID.append(bID)
            sTitle.append(bTitle)
            sGenre.append(bGenre.upper())
            fPrice.append(bPrice)
            sPaperback.append(bPaperback.upper())  
            iOnHand.append(bOnHand)
            sAuthorFirst.append(aFname)
            sAuthorLast.append(aLname)
            sPublisher.append(bPublisher)
            print("Entry stored.")
        junk = input("\nPress Enter to return to the menu.")
                 
    # option3 search the list by book id or title
    elif choice == 3:
        clear()
        print("--------Find Book Entry--------\n")
        found = False
        #prompt user for entry
        searchType = input("Enter the book ID or book title: ")
        #loop through lists
        for x in range(len(sID)):
            #search by id and title
            if (searchType == sID[x] or searchType == sTitle[x]):  
                #print results
                print(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                    str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                    str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                sAuthorLast[x] + ", " + sPublisher[x])
                found = True
        if found == False:            
            print("\nBook not found.")
        junk = input("\nPress Enter to return to the menu.")        
    
                    
    # option4 delete a book in entirety( search for book and delete line)
    elif choice == 4: 
        clear()
        print("------Delete Book Entry------\n")
        found = False
        #prompt user to search for book to delete
        searchID = input("\nPlease enter the book ID or book title you would like to delete: ")
        x = len(sID) - 1 #starts at the end of the list using final index number
        #loop through id and title list searching for the input
        while (x >= 0): #we delete from ending to beginning to avoid invalid indexes
            if (searchID == sID[x] or searchID == sTitle[x]):
                found = True
                #print and validate choice if found
                print(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                    str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                    str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                    sAuthorLast[x] + ", " + sPublisher[x])
                decision = input("Would you like to delete this book? (Y/N): ")
                #delete entry line
                if (decision.upper() == "Y"):
                    del sID[x]
                    del sTitle[x]
                    del sGenre[x]
                    del fPrice[x]
                    del sPaperback[x]
                    del iOnHand[x]
                    del sAuthorFirst[x]
                    del sAuthorLast[x]
                    del sPublisher[x] 
            x -= 1 #causes the search to go backwards till it exits the loop  
        if (found == True):
            print("\nBook deleted.")
        else:
            #if not found or testing if record was actually deleted
            print("\nBook not found.")
        junk = input("\nPress Enter to return to the menu.")    
    # option5 write the complete list to output.txt
    elif choice == 5:
        clear()
        print("------Write Book List to File------\n")
        #create a writeable file
        file2 = open("output.txt", "w")
        #loop through lists
        for x in range(len(sID)):
            #write the lists as lines to the file
            file2.write(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                    str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                    str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                    sAuthorLast[x] + ", " + sPublisher[x] + "\n")
        print("\nList is stored in output.txt.")
        file2.close()
        junk = input("\nPress Enter to return to the menu.")
    # option6 exit program
    elif choice == 0:
        print("\nExiting program...")
        #update setinal value
        go = "N"



