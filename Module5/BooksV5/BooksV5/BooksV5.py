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
