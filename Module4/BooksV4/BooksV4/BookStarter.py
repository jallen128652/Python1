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

x = printMenu()
print(x)
#prompt user for menu option
# option1 iterate through list with one book per line
# option2 take inputs and append list and file
# option3 search the list by book id or title
# option4 delete a book in entirety( search for book and delete line)
# option5 write the complete list to output.txt
# option6 quit (need a loop)

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