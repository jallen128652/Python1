# Author: James Allen 
# Course: ITSE 1373 7P1
# Program Name: BooksV6
# Description: This program manipulates the book.txt file, stores a list
# of obj's, prints, adds new entries, outputs to files and conducts error
# handling. It now has a GUI component that allows user interaction via book viewer.

# Note: Remember to save often and commit to git once tested

#import modules
import os
import BookClass as bc
import Helper as h
import re
import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

#clear fx
clear = lambda: os.system('cls')

#create list for objects
books = []
books2 = []
#create vars for items
sID = ""
sTitle = ""
sGenre = ""
fPrice = 0.0
sPaperback = ""
iOnHand = 0
sAuthorFirst = ""
sAuthorLast = ""
sPublisher = ""

#open and read file
file1 = open("book.txt", "r")

#loop through file line by line
for sLine in file1:
    #separate and strip data
    record = sLine.strip().split(",")
    #store in lists
    sID = record[0].strip()
    sTitle = record[1].strip()
    sGenre = record[2].strip()
    fPrice = float(record[3].strip())
    sPaperback = record[4].strip()  
    iOnHand = int(record[5].strip())
    sAuthorFirst = record[6].strip()
    sAuthorLast = record[7].strip()
    sPublisher = record[8].strip()
    #instantiate BookClass obj's and add line of values to obj's, store in books list
    books.append(bc.BookClass(sID, sTitle, sGenre, fPrice, sPaperback, iOnHand, sAuthorFirst, sAuthorLast, sPublisher))
#close file   
file1.close()    


#loop control val
go = "Y" #sentinal val
#loop until user exits
while (go.upper() == "Y"):
    #call menu fx from helper.py
    h.printMenu()
    #prompt for user input choice
    choice = int(input("\nEnter a menu option number: "))
    # option1 iterate through list with one book per line
    if choice == 1: 
        #clear menu
        clear()
        print("--------View Books Entry--------\n")
        #loop through books list and call printBookInfo()
        for x in books:
            x.printBookInfo()
        #return to menu    
        junk = input("\nPress Enter to return to the menu.")    
    # option2 take inputs and append list and file
    elif choice == 2:
        clear()
        print("--------Add Book Entry--------\n")
        sID = str(input("Please enter the 4 digit book ID: ")) 
        #call fx in helper.py to validate the book id and loop till correct
        while h.isValidID(sID) == False:                   
            if h.isValidID(sID) == False:
                print("Invalid ID entry.")
                sID = str(input("Please enter the 4 digit book ID: "))
        #recieve the rest of the inputs and store to vars        
        sTitle = input("Please enter the book title: ")
        sGenre = input("FIC = fiction, PSY = Psychology, SFI = SciFi, MYS = Mystery, HOR = Horror\nCMP = Computers, ART = Art, PHI = Philosophy, POE = Poetry, TRA = Travel\nPlease enter the book genre 3 letter code: ")
        fPrice = float(input("Please enter the book price: $"))
        sPaperback = input("Paperback? (Y/N): ")
        iOnHand = int(input("How many currently on hand? "))
        sAuthorFirst = input("Please enter the authors first name: ")
        sAuthorLast = input("Please enter the authors last name: ")
        sPublisher = input("Please enter the publishers name: ")
        #print and validate the entry
        print("\nYou entered: " + sID + " " + sTitle + " " + 
              sGenre + " " + "${:,.2f}".format(fPrice) + " " + sPaperback + " " +
              str(iOnHand) + " " + sAuthorFirst + " " + sAuthorLast + " " +
              sPublisher)
        choice2 = input("\nSave this entry? (Y/N): ")
        #store the entry
        if choice2.upper() == "Y":
            books.append(bc.BookClass(sID, sTitle, sGenre, fPrice, sPaperback, iOnHand, sAuthorFirst, sAuthorLast, sPublisher))
            print("Entry stored.")
        else:
            print("Entry discarded.")
        junk = input("\nPress Enter to return to the menu.")
                 
    # option3 search the list by book id or title
    elif choice == 3:
        clear()
        print("--------Find Book Entry--------\n")
        found = False
        #prompt user for entry
        searchType = input("Enter the book ID or book title: ")
        #loop through lists
        for x in books:
            #search by id and partial title
            if searchType == x.id or re.search(searchType, x.title):  
                #print results
                x.printBookInfo()
                found = True
        if found == False:            
            print("\nBook not found.")
        junk = input("\nPress Enter to return to the menu.")        
    
                    
    # option4 delete a book in entirety( search for book and delete line)
    elif choice == 4: 
        clear()
        print("------Delete Book Entry------\n")
        found = False
        #prompt user to search for book to delete
        searchType = input("\nPlease enter the book ID or book title you would like to delete: ")
        x = len(books) - 1 #starts at the end of the list using final index number
        #x = -1 #test for the exception and exit, uncomment to use
        #throws an exception if the loop control calc is out of range
        try:
            if x < 0:
                raise ValueError("Book search out of range, exiting program.")        
            #loop through id and title list searching for the input
            while (x >= 0): #we delete from ending to beginning to avoid invalid indexes
                #search by id and partial title
                if searchType == books[x].id or re.search(searchType, books[x].title):
                    found = True
                    #print and validate choice if found
                    books[x].printBookInfo()
                    decision = input("Would you like to delete this book? (Y/N): ")
                    #delete entry line
                    if (decision.upper() == "Y"):
                        #deletes the object they were stored in
                        del books[x]
                x -= 1 #causes the search to go backwards till it exits the loop  
            if (found == True and decision.upper() == "Y"):
                print("\nBook deleted.")
            elif (found == True and decision.upper() == "N"):
                print("\nBook not deleted.")
            else:
                print("\nBook not found.")
            junk = input("\nPress Enter to return to the menu.") 
        except ValueError:
            print("Book search out of range, exiting program.")
            quit()
    # option5 write the complete list to output.txt
    elif choice == 5:
        clear()
        print("------Write Book List to File------\n")
        #create a writeable file
        file2 = open("output.txt", "w")
        #loop through books list and calls BookClass fx
        for x in books:
            x.writeBookInfo(file2)
        print("\nList is stored in output.txt.")
        file2.close()
        junk = input("\nPress Enter to return to the menu.")
    #option6 Book Viewer GUI
    elif choice == 6:
        #create window
        window = tk.Tk()
        window.title("Book Viewer")
        window.geometry('300x160')
        window.resizable(0, 0)
        #functions for the three buttons
        def openFile():
            #global vars and lists
            global books2, x
            global file3
            global entryvar1, entryvar2, entryvar3, entryvar4, entryvar5, entryvar6, entryvar7, entryvar8, entryvar9
            #declare global accumulator
            x = 0
            #open the book.txt file
            try:
                file3 = open("book.txt", "r")
                #Load the file records into a List of BookClass objects
                for sLine in file3:
                #separate and strip data
                    record = sLine.strip().split(",")
                    #store in lists
                    sID = record[0].strip()
                    sTitle = record[1].strip()
                    sGenre = record[2].strip()
                    fPrice = float(record[3].strip())
                    sPaperback = record[4].strip()  
                    iOnHand = int(record[5].strip())
                    sAuthorFirst = record[6].strip()
                    sAuthorLast = record[7].strip()
                    sPublisher = record[8].strip()
                    #instantiate BookClass obj's and add line of values to obj's, store in books list
                    books2.append(bc.BookClass(sID, sTitle, sGenre, fPrice, sPaperback, iOnHand, sAuthorFirst, sAuthorLast, sPublisher))
                file3.close()
            #Display the first book or give a message box error if the file is empty
                if len(books2) > 0:
                    #sets the first book into the entryvars1-9
                    entryvar1.set(books2[x].id)
                    entryvar2.set(books2[x].title)
                    entryvar3.set(books2[x].genre)
                    entryvar4.set(str(books2[x].price))
                    entryvar5.set(books2[x].paperback)
                    entryvar6.set(str(books2[x].onHand))
                    entryvar7.set(books2[x].authorFname)
                    entryvar8.set(books2[x].authorLname)
                    entryvar9.set(books2[x].publisher)
                else:
                    showerror("Error", "Booklist is empty")
            except FileNotFoundError:
                showerror("Error", "File not found")
        def nextBook():
            #the function displays the next record in the book List.   
            global books2, x
            global entryvar1, entryvar2, entryvar3, entryvar4, entryvar5, entryvar6, entryvar7, entryvar8, entryvar9
            #Gives a message box if the booklist is empty.
            if len(books2) == 0:
                showinfo("Info", "Booklist is empty") 
            #add 1 to x
            x += 1
            #Ensures you don't go past the end of List.
            if x < len(books2):                
                #sets the next book vals
                entryvar1.set(books2[x].id)
                entryvar2.set(books2[x].title)
                entryvar3.set(books2[x].genre)
                entryvar4.set(str(books2[x].price))
                entryvar5.set(books2[x].paperback)
                entryvar6.set(str(books2[x].onHand))
                entryvar7.set(books2[x].authorFname)
                entryvar8.set(books2[x].authorLname)
                entryvar9.set(books2[x].publisher)                
            else:
                #lets you know you reached the end
                showinfo("Info", "You have reached the end of the list.")
        def prevBook():
            #the function displays the next record in the book List.   
            global books2, x
            global entryvar1, entryvar2, entryvar3, entryvar4, entryvar5, entryvar6, entryvar7, entryvar8, entryvar9
            #Gives a message box if the booklist is empty.
            if len(books2) == 0:
                showinfo("Info", "Booklist is empty")
            #subtract 1 from x
            x -= 1
            #Ensures you don't go out of list bounds.
            if x >= 0:
                #sets the previous book vals
                entryvar1.set(books2[x].id)
                entryvar2.set(books2[x].title)
                entryvar3.set(books2[x].genre)
                entryvar4.set(str(books2[x].price))
                entryvar5.set(books2[x].paperback)
                entryvar6.set(str(books2[x].onHand))
                entryvar7.set(books2[x].authorFname)
                entryvar8.set(books2[x].authorLname)
                entryvar9.set(books2[x].publisher)                
            else:
                #lets you know you reached the beginning of the list
                showinfo("Info", "You have reached the beginning of the list.")
        #config window dimensions and grid
        window.rowconfigure(0, minsize=7, weight=1)
        window.rowconfigure(1, minsize=7, weight=1)
        window.rowconfigure(2, minsize=7, weight=1)
        window.rowconfigure(3, minsize=7, weight=1)
        window.rowconfigure(4, minsize=7, weight=1)
        window.rowconfigure(5, minsize=7, weight=1)
        window.rowconfigure(6, minsize=7, weight=1)
        window.rowconfigure(7, minsize=7, weight=1)
        window.rowconfigure(8, minsize=7, weight=1)
        window.rowconfigure(9, minsize=12, weight=1)
        window.columnconfigure(0, minsize=20, weight=1)
        window.columnconfigure(1, minsize=20, weight=1)
        window.columnconfigure(2, minsize=60, weight=3)
        #create buttons on first column
        btn_opn = tk.Button(window, text="Open", command=openFile)
        btn_opn.grid(row=9, column=0, ipadx=8, pady=3, padx=3)        
        btn_nxt = tk.Button(window, text="Next", command=nextBook)
        btn_nxt.grid(row=9, column=1, ipadx=10, padx=10, pady=3, sticky="e")      
        btn_prv = tk.Button(window, text="Previous", command=prevBook)
        btn_prv.grid(row=9, column=2, pady=3, padx=50, sticky="e")
        #create labels on the second column
        label1 = tk.Label(window, text='ID')
        label1.grid(column=1, row=0, sticky="w") 
        label2 = tk.Label(window, text='Title')
        label2.grid(column=1, row=1, sticky="w")
        label3 = tk.Label(window, text='Genre')
        label3.grid(column=1, row=2, sticky="w")
        label4 = tk.Label(window, text='Price')
        label4.grid(column=1, row=3, sticky="w")
        label5 = tk.Label(window, text='Paperback')
        label5.grid(column=1, row=4, sticky="w") 
        label6 = tk.Label(window, text='On Hand')
        label6.grid(column=1, row=5, sticky="w")
        label7 = tk.Label(window, text='First Name')
        label7.grid(column=1, row=6, sticky="w")
        label8 = tk.Label(window, text='Last Name')
        label8.grid(column=1, row=7, sticky="w")
        label8 = tk.Label(window, text='Publisher')
        label8.grid(column=1, row=8, sticky="w")
        #create entries on the third column
        entryvar1 = tk.StringVar()
        entry1 = tk.Entry(window, textvariable=entryvar1)
        entry1.grid(column=2, row=0, pady=1, padx=2)
        entry1.focus()
        entryvar2 = tk.StringVar()
        entry2 = tk.Entry(window, textvariable=entryvar2)
        entry2.grid(column=2, row=1, pady=1, padx=2)
        entry2.focus()
        entryvar3 = tk.StringVar()
        entry3 = tk.Entry(window, textvariable=entryvar3)
        entry3.grid(column=2, row=2, padx=2, pady=1)
        entry3.focus()
        entryvar4 = tk.StringVar()
        entry4 = tk.Entry(window, textvariable=entryvar4)
        entry4.grid(column=2, row=3, pady=1, padx=2)
        entry4.focus()
        entryvar5 = tk.StringVar()
        entry5 = tk.Entry(window, textvariable=entryvar5)
        entry5.grid(column=2, row=4, padx=2, pady=1)
        entry5.focus()
        entryvar6 = tk.StringVar()
        entry6 = tk.Entry(window, textvariable=entryvar6)
        entry6.grid(column=2, row=5, pady=1, padx=2)
        entry6.focus()
        entryvar7 = tk.StringVar()
        entry7 = tk.Entry(window, textvariable=entryvar7)
        entry7.grid(column=2, row=6, padx=2, pady=1)
        entry7.focus()
        entryvar8 = tk.StringVar()
        entry8 = tk.Entry(window, textvariable=entryvar8)
        entry8.grid(column=2, row=7, pady=1, padx=2)
        entry8.focus()
        entryvar9 = tk.StringVar()
        entry9 = tk.Entry(window, textvariable=entryvar9)
        entry9.grid(column=2, row=8, padx=2, pady=1)
        entry9.focus()
        #event handler and listener fx from Tkinter
        window.mainloop()
    # option7 exit program
    elif choice == 0:
        print("\nExiting program...")
        #update setinal value
        go = "N"
