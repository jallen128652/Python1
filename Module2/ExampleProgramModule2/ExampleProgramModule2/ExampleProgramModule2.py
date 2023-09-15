#***********************NOTES FOR M1 LESSON4*********************
#***************complete program example****************
# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: Example
# Description: An example for module 2

#basic program structure
# 1. Top documentation
# 2. vars and consts declarations
# 3. user input
# 4. calculations/processing
# 5. output

#consts section
INCOME_TAX_RATE = 0.22

#prompt asking if you want to start the loop
sRepeat = input("Do you want to calculate income tax? (y/n)")
#while loop
while sRepeat.upper() == "Y":
 #indent rest of the program to become part of the while loop
	#input vars section
	sFName = ""
	sLName = ""
	sSSN = "" # never used for calc so store as string
	iAge = 0
	fPayRate = 0.0
	fHoursWorked = 0.0

	#calculated vars section
	fTaxDeduction = 0.0
	fGrossPay = 0.0
	fNetPay = 0.0

	#get user input section
	print("Simple Tax Calculator \n\n")
	sFName = input("\t Enter First Name: ")
	sLName = input("\t Enter Last Name: ")
	sSSN = input("\t Enter Social Security Number (555-55-5555): ")

	iAge = int(input("\t Enter Age: "))
	fPayRate = float(input("\t Enter Hourly Pay Rate: "))
	fHoursWorked = float(input("\t Enter Hours Worked: "))

	#calculations
	# work it out on paper first
	# make sure you understand the problem
	# just because there's no syntax errors and you recieve values doesn't mean the
	#  logic is correct
	fGrossPay = fHoursWorked * fPayRate
	fTaxDeduction = fGrossPay * INCOME_TAX_RATE
	fNetPay = fGrossPay - fTaxDeduction

	#output
	print("---------------------------\n\n")
	# User ID is the first initial + last name + last 4 of SSN
				#char[0] of the var		#char[7] of the var to the end
	print("User ID: " + sFName[0:1] + sLName + sSSN[7:] + "\n")
				#formats fGrossPay float to 2 decimal places
	print("Gross Pay: ${:,.2f}".format(fGrossPay))
				#formats fTaxDeduction float to 2 decimal places
	print("Tax Deduction: ${:,.2f}".format(fTaxDeduction))
				#formats fNetPay float to 2 decimal places
	print("Net Pay: ${:,.2f}".format(fNetPay))
	#update loop control var
	sRepeat = input("Do you want to calculate another income tax? (y/n)")
