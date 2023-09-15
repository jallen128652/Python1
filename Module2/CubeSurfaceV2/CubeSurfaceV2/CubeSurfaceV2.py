# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: CubeSurfaceV2
# Description: Calculates the surface area of a cube in feet and meters
# as many times as the user wants.
# Note: Remember to save often and commit to git once tested

#Instructions:
#Write a program that calculates the surface area of a cube in feet and meters.
# A cube is made up of 6 squares of equal size. The surface area of a cube can be
#  calculated with the formula 6 * sideLength * sideLength. To convert feet to
#   meters, divide total feet by 10.765.

#consts section
FEET_TO_METERS = 10.765

#input vars section
cubeSide = 0.0

#calculated vars section
cubeSurfaceFeet = 0.0
cubeSurfaceMeters = 0.0

#get user input section
print("Welcome to the Cube Surface Calculator! \n\n")
cubes = input("Would you like to calculate the surface area of a cube? (y/n) ")
# looks until the user enters n
while cubes.upper() == "Y":
# casts the input as a float
	cubeSide = float(input("Enter a side lenght of a cube in feet: "))

	#calculations 
	cubeSurfaceFeet = 6 * cubeSide * cubeSide
	cubeSurfaceMeters = cubeSurfaceFeet / FEET_TO_METERS

	#output
		#results separator
	print("_____________________________________________________\n")
	# formats the float vals to 2 decimal precision
	print("The surface area of the cube is: {:,.2f}".format(cubeSurfaceFeet) + " square feet")
	print("The surface area of the cube is: {:,.2f}".format(cubeSurfaceMeters) + " square meters\n")
	# updates the loop control var
	cubes = input("Would you like to calculate the surface area of another cube? (y/n) ")