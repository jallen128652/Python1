# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BooksV3
# Description: This program manipulates the book.txt file and prints
# Note: Remember to save often and commit to git once tested

#Instructions: Write a python script that does the following:

#These records represent data for a book. this is what the 9 elements represent:

#BookID, Title, Genre, Price, Paperback, AmountInInventory, AuthorFirst,
# AuthorLast, Publisher

#Program requirements:

# The program will separate each record line into variables. Use a name similar
#  to the bolded 9 elements line above.
# As you process each line, you will create 3 output files.

# File2 will write to output.txt. Write all the records with a | (pipe) delimiter
# instead of a comma.  Pipe is above the Enter key.  One record per line,
#  write out all items.

# File3 will write to reorder.txt. Write out lines with the elements BookID,
#  Title, Price, and AmoutInInventory.  Only write out lines whose 
#  Price * AmountInInventory is less than 50 dollars.  These are the books to
#   reorder.

# File4 will write to mystery.txt. Write out only the title for all books whose
#  Genre is mystery “MYS”

#opens book.txt for read
file = open("book.txt", "r")
#creates and opens writeable files
file2 = open("output.txt", "w")
file3 = open("reorder.txt", "w")
file4 = open("mystery.txt", "w")
#loops through the linestrings storing the line list items in list vars
for lineString in file:
    lineList = lineString.strip().split(",")
    bookId = lineList[0]
    title =  lineList[1]
    genre = lineList[2]
    price = lineList[3]
    paperBack = lineList[4]
    amountInInventory = lineList[5]
    authorFname = lineList[6]
    authorLname = lineList[7]
    publisher = lineList[8]