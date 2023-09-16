# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BooksV2
# Description: This program provides book inventory data by title or ISBN

#Instructions:
#The program should
#  loop to ask for multiple books data, entered at the console. After getting the
#   information for a book, print the following in comma-delimited format. Last
#    4 characters of ISBN, First 5 letters of Title, Number on hand, price *
#     on hand with 2 decimal places.
#vars and consts
bookData = []

#get user input section
print("Welcome to the Bookstore! \n\n")
books = input("Would you like to add a book title order? (y/n) ")
# looks until the user enters n
while books.upper() == "Y":
	#body of the loop
	#inputs
	ISBN = input("\nEnter the 10 digit ISBN: ")
	title = input("Enter the book title: ")
	genre = input("Enter the 3 letter book genre code: \n Mystery = MYS, Fantasy = FSY, SciFi = SCI, Non-Fiction = NFI: ")
	# casts the input as a float
	price = float(input("Enter the price of the book: $"))
	paperBack = input("Do you want paperback? (y/n): ")
	# casts the input as a int
	onHand = int(input("How many copies are on hand?: "))

	#calculations 
	qtyPrice = price * onHand	
	genre = genre.upper()
	#append the data to list 
	bookData.append(ISBN[-4:])
	bookData.append(title[0:5])
	bookData.append(onHand)
	bookData.append("Sub total: ${:,.2f}".format(qtyPrice))
	#output
	#results separator
	print("________________________________________\n")
	print("Your order details:\n")
	#print list in comma delimited format	
	print(*bookData, sep = ", ")
	#above = print(bookData[0] + ", " + bookData[1] + ", " + str(bookData[2]) + ", " + str(bookData[3])) 
	#updates loop control var
	books = input("Would you like to add another book title order? (y/n) ")