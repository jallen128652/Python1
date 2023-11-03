# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: helper
# Description: This program is a module that maintains fx's for use in other programs

#imports
import os
#clear fx
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
#id validator fx
def isValidID(sID):    
    num1 = len(sID)
    if num1 == 4:   
        #check book ID for duplicates and raise an error
        with open("book.txt", "r") as file:
            for line in file:
                if sID in line.strip().split(","):
                    raise ValueError("Duplicate ID found.")
        return True        
    else:
        return False
    
    


    

