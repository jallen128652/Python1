# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BooksV6
# Description: This program manipulates the book.txt file and prints
# Note: Remember to save often and commit to git once tested

#import modules
import os
import BookClass as bc
import Helper as h
import re

#clear fx
clear = lambda: os.system('cls')

#create list for objects
books = []

#create vars for items
sID = ""
sTitle = ""
sGenre = ""
fPrice = 0.0
sPaperback = ""
iOnHand = 0
sAuthorFirst = ""
sAuthorLast = ""
sPublisher = ""

#open and read file
file1 = open("book.txt", "r")

#loop through file line by line
for sLine in file1:
    #separate and strip data
    record = sLine.strip().split(",")
    #store in lists
    sID = record[0].strip()
    sTitle = record[1].strip()
    sGenre = record[2].strip()
    fPrice = float(record[3].strip())
    sPaperback = record[4].strip()  
    iOnHand = int(record[5].strip())
    sAuthorFirst = record[6].strip()
    sAuthorLast = record[7].strip()
    sPublisher = record[8].strip()
    #instantiate BookClass obj's and add line of values to obj's, store in books list
    books.append(bc.BookClass(sID, sTitle, sGenre, fPrice, sPaperback, iOnHand, sAuthorFirst, sAuthorLast, sPublisher))
#close file   
file1.close()    


#loop control val
go = "Y" #sentinal val
#loop until user exits
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
        #loop through books list and call printBookInfo()
        for x in books:
            x.printBookInfo()
        #return to menu    
        junk = input("\nPress Enter to return to the menu.")    
    # option2 take inputs and append list and file
    elif choice == 2:
        clear()
        print("--------Add Book Entry--------\n")
        sID = str(input("Please enter the 4 digit book ID: ")) 
        #call fx in helper.py to validate the book id and loop till correct
        while h.isValidID(sID) == False:                   
            if h.isValidID(sID) == False:
                print("Invalid ID entry.")
                sID = str(input("Please enter the 4 digit book ID: "))
        #recieve the rest of the inputs and store to vars        
        sTitle = input("Please enter the book title: ")
        sGenre = input("FIC = fiction, PSY = Psychology, SFI = SciFi, MYS = Mystery, HOR = Horror\nCMP = Computers, ART = Art, PHI = Philosophy, POE = Poetry, TRA = Travel\nPlease enter the book genre 3 letter code: ")
        fPrice = float(input("Please enter the book price: $"))
        sPaperback = input("Paperback? (Y/N): ")
        iOnHand = int(input("How many currently on hand? "))
        sAuthorFirst = input("Please enter the authors first name: ")
        sAuthorLast = input("Please enter the authors last name: ")
        sPublisher = input("Please enter the publishers name: ")
        #print and validate the entry
        print("\nYou entered: " + sID + " " + sTitle + " " + 
              sGenre + " " + "${:,.2f}".format(fPrice) + " " + sPaperback + " " +
              str(iOnHand) + " " + sAuthorFirst + " " + sAuthorLast + " " +
              sPublisher)
        choice2 = input("\nSave this entry? (Y/N): ")
        #store the entry
        if choice2.upper() == "Y":
            books.append(bc.BookClass(sID, sTitle, sGenre, fPrice, sPaperback, iOnHand, sAuthorFirst, sAuthorLast, sPublisher))
            print("Entry stored.")
        else:
            print("Entry discarded.")
        junk = input("\nPress Enter to return to the menu.")
                 
    # option3 search the list by book id or title
    elif choice == 3:
        clear()
        print("--------Find Book Entry--------\n")
        found = False
        #prompt user for entry
        searchType = input("Enter the book ID or book title: ")
        #loop through lists
        for x in books:
            #search by id and partial title
            if searchType == x.id or re.search(searchType, x.title):  
                #print results
                x.printBookInfo()
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
        searchType = input("\nPlease enter the book ID or book title you would like to delete: ")
        x = len(books) - 1 #starts at the end of the list using final index number
        #x = -1 #test for the exception and exit
        #throws an exception if the loop control calc is out of range
        try:
            if x < 0:
                raise ValueError("Book search out of range, exiting program.")        
            #loop through id and title list searching for the input
            while (x >= 0): #we delete from ending to beginning to avoid invalid indexes
                #search by id and partial title
                if searchType == books[x].id or re.search(searchType, books[x].title):
                    found = True
                    #print and validate choice if found
                    books[x].printBookInfo()
                    decision = input("Would you like to delete this book? (Y/N): ")
                    #delete entry line
                    if (decision.upper() == "Y"):
                        #deletes the object they were stored in
                        del books[x]
                x -= 1 #causes the search to go backwards till it exits the loop  
            if (found == True and decision.upper() == "Y"):
                print("\nBook deleted.")
            elif (found == True and decision.upper() == "N"):
                print("\nBook not deleted.")
            else:
                print("\nBook not found.")
            junk = input("\nPress Enter to return to the menu.") 
        except ValueError:
            print("Book search out of range, exiting program.")
            quit()
    # option5 write the complete list to output.txt
    elif choice == 5:
        clear()
        print("------Write Book List to File------\n")
        #create a writeable file
        file2 = open("output.txt", "w")
        #loop through books list and calls BookClass fx
        for x in books:
            x.writeBookInfo(file2)
        print("\nList is stored in output.txt.")
        file2.close()
        junk = input("\nPress Enter to return to the menu.")
    # option6 exit program
    elif choice == 0:
        print("\nExiting program...")
        #update setinal value
        go = "N"
