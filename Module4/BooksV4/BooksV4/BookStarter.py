# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BookStarter
# Description: This program manipulates the book.txt file and prints
# Note: Remember to save often and commit to git once tested

#Instructions:


import os
#prompt user for menu option
def printMenu():
    clear()
    print("-------- Menu --------\n")
    print("1. View Books Entry")
    print("2. Add Book Entry")
    print("3. Find Book Entry")
    print("4. Delete Book Entry")
    print("5. Write Book List to File")    
    print("0. Quit")


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

printMenu()

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


#prompt user for menu option
choice = int(input("Enter a menu option number: "))
while choice != 0:
    # option1 iterate through list with one book per line
    if choice == 1: 
        for x in range(len(sID)):
            print(str(sID[x]) + ", " + sTitle[x] + ", " + sGenre[x] + ", " +
                  str(fPrice[x]) + ", " + sPaperback[x] + ", " +
                 str(iOnHand[x]) + ", " + sAuthorFirst[x] + ", " +
                sAuthorLast[x] + ", " + sPublisher[x])
        done = input("\nOnce you complete reviewing the list enter Y to return to the main menu: ")
        if done.upper() == "Y":
            printMenu()
            choice = int(input("Enter a menu option number: "))     
    # option2 take inputs and append list and file
    elif choice == 2:
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
            printMenu()
            choice = int(input("Enter a menu option number: "))
        else:
            printMenu()
            choice = int(input("Enter a menu option number: "))
                 
    # option3 search the list by book id or title
    elif choice == 3:
        print("search for book")
    # option4 delete a book in entirety( search for book and delete line)
    elif choice == 4:
        print("delete book")
    # option5 write the complete list to output.txt
    elif choice == 5:
        print("save to file")
    # option6 quit (need a loop)



