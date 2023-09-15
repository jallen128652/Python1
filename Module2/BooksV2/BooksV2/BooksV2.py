# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BooksV2
# Description: Calculates the total price for books with taxes
# Note: Remember to save often and commit to git once tested

#Instructions:
#Calculate the total price for books with tax

#consts section
TAX_RATE = 0.0825

#input vars section
bookName = ""
bookPrice = 0.0
numCopies = 0

#calculated vars section
subTotal = 0.0
taxes = 0.0
total = 0.0

#get user input section
print("Welcome to the Bookstore! \n\n")
bookName = input("Enter the name of the book: ")
# casts the input as a float
bookPrice = float(input("Enter the price of the book: "))
# casts the input as a int
numCopies = int(input("Enter the number of copies you wish to purchase: "))

#calculations 
subTotal = bookPrice * numCopies
taxes = subTotal * TAX_RATE
total = subTotal + taxes

#output
	#results separator
print("________________________________________\n")
print("Your order details:\n")
# casts int to str so the concat doesn't throw an error
print("You selected " + str(numCopies) + " copies of: " + bookName)
# formats the float vals to 2 decimal precision
print("Subtotal is: ${:,.2f}".format(subTotal))
print("Tax is: ${:,.2f}".format(taxes))
print("Total due is: ${:,.2f}".format(total))
print("\nThanks for shopping at the Bookstore!")
