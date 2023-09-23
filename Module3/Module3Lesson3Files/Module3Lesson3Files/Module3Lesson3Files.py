#***************************Files Notes***********************
"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:
var = open(filename)
file = open("demofile.txt")

The code above is the same as:
var = open(filename, mode)
file = open("demofile.txt", "rt")

**When you are done with the file you must also close using the variable**
file.close()
"""
#Reading a File
#The read() function can read the whole file or a certain number of characters()
"""
file = open("data.txt")
sFirstSix = file.read(6)
print(sFirstSix)
file.close()
"""
#reading the whole file
"""
file = open("data.txt")
sWholeFile = file.read()
print(sWholeFile)
file.close()
"""
#readline() function
#You can read a line at a time using readline. There is however an easier way to
# process a file a line at a time
"""
file = open("data.txt")
sOneLine = file.readline()
sNextLine = file.readline()
file.close()
"""

#Processing a text file
#This text file has one record per line with the following values
#First Name, Last Name, Email, Birth Month, Birth Day, Birth Year
#Be aware if you data has commas naturally, you will need a different delimiter
"""
example file:
data.txt

Bill,Smith,bsmith@noemail.com,2,16,1994
Tony,Lozano,tony.lozano@tstc.edu,8,1,1901
Bill,Doe,bd@gmail.edu,12,30,2001
"""
#Reading and printing one line at a time using a for loop
"""
file = open("data.txt")
for lineString in file:
	print(lineString)
file.close()
"""

"""
file = open("data.txt")
for lineString in file:
    print(lineString)
file.close()
"""

#more usefull version by creating a list and using methods on the lineString
"""
file = open("data.txt")
for lineString in file:
                        #strip extra spaces and split the line at the comma
    lineList = lineString.strip().split(",")
    print(lineList)
file.close()
"""
#prints a list:
"""
['Bill', 'Smith', 'bsmith@noemail.com', '2', '16', '1994']
['Tony', 'Lozano', 'tony.lozano@tstc.edu', '8', '1', '1901']
['Bill', 'Doe', 'bd@gmail.edu', '12', '30', '2001']
"""
#Separating the data
#Now to assign these values to variables
#for birthday we have to import datetime
"""
import datetime
records = 0 #accumulator
file = open("data.txt")
for lineString in file:
    lineList = lineString.strip().split(",")
    firstName = lineList[0]
    lastName = lineList[1]
    email = lineList[2]
    #must be year month day format
    birthDate = datetime.datetime(int(lineList[5]),int(lineList[3]),int(lineList[4]))
    
    print(firstName, lastName, email, birthDate)
    records += 1
  
file.close()
"""

#Writing data (overwrites file)
#Writing is simple. You write to a file just like you print to the screen.
#The write() function doesn’t automatically add a newline
var = 0
of = open("output.txt", "w") #file must exist
of.write("Hello World\n")
of.write("The value of var is: " + str(var) + "\n")
of.close()

#adding to instead of overwriting a file using "a" instead of "w"
of = open("output.txt", "a")
of.write("This line is added\n")
of.close()