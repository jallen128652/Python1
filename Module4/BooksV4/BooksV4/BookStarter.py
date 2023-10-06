# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BookStarter
# Description: This program manipulates the book.txt file and prints
# Note: Remember to save often and commit to git once tested

#Instructions:


import os

import Helper as h

clear = lambda: os.system('cls')

sID = []
sTitle = []
sGenre = []
fPrice = []
sPaperback = []
iOnHand = []
sAuthorFirst = []
sAuthorLast = []
sPublisher = []

file1 = open("book.txt", "r")
for sLine in file1:
    record = sLine.strip().split(",")
    sID.append(record[0].strip())
    sTitle.append(record[1].strip())
    sGenre.append(record[2].strip())
    fPrice.append(float(record[3].strip()))
    sPaperback.append(record[4].strip())  
    iOnHand.append(int(record[5].strip()))
    sAuthorFirst.append(record[6].strip())
    sAuthorLast.append(record[7].strip())
    sPublisher.append(record[8].strip())
file1.close()    

go = "Y" #sentinal val

while (go.upper() == "Y"):
    h.printMenu()
    choice = int(input("Enter a menu option number: "))
    # option1 iterate through list with one book per line
    if choice == 1: 
        clear()
        print("--------View Books Entry--------\n")
        for x in range(len(sID)):
            print(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                  str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                 str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                sAuthorLast[x] + ", " + sPublisher[x])
        junk = input("\nPress Enter to return to the menu.")    
    # option2 take inputs and append list and file
    elif choice == 2:
        clear()
        print("--------Add Book Entry--------\n")
        bID = int(input("Please enter the 4 digit book ID: "))
        bTitle = input("Please enter the book title: ")
        bGenre = input("FIC = fiction, PSY = Psychology, SFI = SciFi, MYS = Mystery, HOR = Horror\nCMP = Computers, ART = Art, PHI = Philosophy, POE = Poetry, TRA = Travel\nPlease enter the book genre 3 letter code: ")
        bPrice = float(input("Please enter the book price: $"))
        bPaperback = input("Paperback? (Y/N): ")
        bOnHand = int(input("How many currently on hand? "))
        aFname = input("Please enter the authors first name: ")
        aLname = input("Please enter the authors last name: ")
        bPublisher = input("Please enter the publishers name: ")
        print("\nYou entered: " + str(bID) + " " + bTitle + " " + 
              bGenre + " $" + str(bPrice) + " " + bPaperback + " " +
              str(bOnHand) + " " + aFname + " " + aLname + " " +
              bPublisher)
        choice2 = input("\nSave this entry and exit to the menu? (Y/N): ")
        if choice2.upper() == "Y":
            sID.append(bID)
            sTitle.append(bTitle)
            sGenre.append(bGenre)
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
        searchType = input("Enter the book ID or book title: ")
        for x in range(len(sID)):
            if (searchType == sID[x] or searchType == sTitle[x]):                 
                print(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                    str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                    str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                sAuthorLast[x] + ", " + sPublisher[x])
                found = True
            else:                
                print("Book not found.")
        junk = input("\nPress Enter to return to the menu.")        
    
                    
    # option4 delete a book in entirety( search for book and delete line)
    elif choice == 4: 
        clear()
        print("------Delete Book Entry------\n")
        found = False
        searchID = input("Please enter the book ID or book title you would like to delete: ")
        x = len(sID) - 1 #starts at the end of the list using final index number
        while (x >= 0): #we delete from ending to beginning to avoid invalid indexes
            if (searchID == sID[x] or searchID == sTitle[x]):
                found = True
                print(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                    str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                    str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                    sAuthorLast[x] + ", " + sPublisher[x])
                decision = input("Would you like to delete this book? (Y/N): ")
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
            print("Book deleted.")
        else:
            print("Book not found.")
        junk = input("\nPress Enter to return to the menu.")    
    # option5 write the complete list to output.txt
    elif choice == 5:
        clear()
        print("------Write Book List to File------\n")
        file2 = open("output.txt", "w")
        for x in range(len(sID)):
            file2.write(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                    str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                    str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                    sAuthorLast[x] + ", " + sPublisher[x] + "\n")
        print("List is stored in output.txt.")
        file2.close()
        junk = input("\nPress Enter to return to the menu.")
    # option6 exit program
    elif choice == 0:
        print("Exiting program...")
        go = "N"



