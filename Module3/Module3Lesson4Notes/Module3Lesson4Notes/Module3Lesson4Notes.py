#********************Complete program example***********************
import os
clear = lambda: os.system('cls') #clears the screen of the menu and prints the choice

#use empty array or dummy record initially
fname = ["Bill", "Tony", "Bill"]
lname = ["Smith", "Lozano", "Doe"]
email = ["bsmith@noemail.com", "tonylozano@tstc.edu", "bd@gmail.edu"]
#fname = []
#lname = []
#email = []

go = "Y" #sentinel value

while (go.upper() == "Y"):
    clear()
    print("--------Menu--------\n")
    print("1. View List")
    print("2. Add Entry")
    print("3. Find Entry")
    print("4. Delete Entry")
    print("5. Quit")
    choice = int(input("\nEnter Selection: "))
    
    if (choice == 1):
        clear()
        print("--------View List--------\n")
        for x in range(len(fname)):
            print(fname[x] + ", " + lname[x] + ", " + email[x])
        junk = input("\nPress Enter to return to the menu.")
        
    elif (choice == 2):
        clear()
        print("--------Add Entry--------\n")
        f = input("Enter First Name: ")
        l = input("Enter Last Name: ")
        e = input("Enter Email: ")
        addchoice = input("Add this entry? (Y/N): ")
        if (addchoice.upper() == "Y"):
            fname.append(f)
            lname.append(l)
            email.append(e)
        junk = input("\nPress Enter to return to the menu.")
        
    elif (choice == 3):
        clear()
        print("--------Find Entry--------\n")
        searchname = input("Enter the first or last name of person: ")
        for x in range(len(fname)):
            if (searchname == fname[x] or searchname == lname[x]):
                print(fname[x] + ", " + lname[x] + ", " + email[x])
        junk = input("\nPress Enter to return to the menu.")
        
    elif (choice == 4):
        clear()
        print("--------Delete Entry--------\n")
        
        found = False
        searchname = input("Enter the first or last name of person: ")
        x = len(fname) - 1 #starts at the end of the list using final index number
        while (x >= 0): #we delete from ending to beginning to avoid invalid indexes
            if (searchname == fname[x] or searchname == lname[x]):
                found = True
                print(fname[x] + ", " + lname[x] + ", " + email[x])
                delchoice = input("Delete? (Y/N): ")
                if (delchoice.upper() == "Y"):
                    del fname[x]
                    del lname[x]
                    del email[x]
            x -= 1 #causes the search to go backwards till it exits the loop  
        if (found == True):
            print("No more records found.")
        else:
            print("No records found.")
        junk = input("\nPress Enter to return to the menu.")  
        
    elif (choice == 5): #remember indentation so it stays in the code block
        clear()
        go = "N" # exits the program next loop
    else:
        print("Invalid Entry! Press Enter.")
        continue #continues the loop back to the input var