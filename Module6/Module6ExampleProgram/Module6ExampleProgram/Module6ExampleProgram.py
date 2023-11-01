#***********************Example Program*******************
"""
Complete Program
- A common thing programmers do is update data
- In this program we will be using regex to update incorrect data files
"""
# note we don't have the inventory.txt to validate this progrm :(
import re

file = open("inventory.txt")
of = open("output.txt")

for readline in file:
        # begins with 44, has a space and begins with SAN and any char after
    if re.search("^44\sSAN.", readline) != None:
        #print(readline) # shows which lines will be changed before you change
        x = re.sub("^44\sSAN.", "44 SAND", readline)
        of.write(x) # writes the changed lines to output file
    else:
        of.write(readline) # writes the lines to output that don't get changed

file.close()
of.close()
