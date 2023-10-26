# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BooksV5
# Description: This program manipulates the book.txt file and prints
# Note: Remember to save often and commit to git once tested

#import modules
import os
import BookClass as bc
import Helper as h

#clear fx
clear = lambda: os.system('cls')

#create list for objects
books = []

#create lists for items
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

#loop through lists and store in BookClass objects
for x in range(len(sID)):
    books.append(bc.BookClass(sID[x], sTitle[x], sGenre[x], fPrice[x], sPaperback[x], iOnHand[x], sAuthorFirst[x], sAuthorLast[x], sPublisher[x]))

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
       
        junk = input("\nPress Enter to return to the menu.")
                 
    # option3 search the list by book id or title
    elif choice == 3:
        clear()
        print("--------Find Book Entry--------\n")
        
        junk = input("\nPress Enter to return to the menu.")        
    
                    
    # option4 delete a book in entirety( search for book and delete line)
    elif choice == 4: 
        clear()
        print("------Delete Book Entry------\n")
       
        junk = input("\nPress Enter to return to the menu.")    
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