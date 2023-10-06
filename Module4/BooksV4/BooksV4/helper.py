# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: helper
# Description: This program is a module that maintains fx's for use in other programs

import os

clear = lambda: os.system('cls')
# menu fx
def printMenu():
    clear()
    print("-------- Menu --------\n")
    print("1. View Books Entry")
    print("2. Add Book Entry")
    print("3. Find Book Entry")
    print("4. Delete Book Entry")
    print("5. Write Book List to File")    
    print("0. Quit")

def isValidID(bID):
    num1 = len(str(abs(bID)))
    if num1 == 4:
        return True
    else:
        return False