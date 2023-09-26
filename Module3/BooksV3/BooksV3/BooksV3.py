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
