

import re


# Module 6 RegExp Mastery

# When running, use the input to test your solution
#  You can if you wish comment out completed problems to simplify testing
text = input("Enter text to test the individual problem you are testing: ")




#-------------------------------------------------------------------
# Problem 1 Instructions
#  In the quotes write the regular expression that matches the letters
#  "Tex" (no quotes) anywhere in the string.

x = re.search("Change Me", text)

if x == None:
    print("No Tex Anywhere Match!")
else:
    print("Tex Anywhere Match!")


#-------------------------------------------------------------------
# Problem 2 Instructions
#  In the quotes write the regular expression that matches the letters
#  "Tex" (no quotes) at the beginning of the string.

x = re.search("Change Me", text)

if x == None:
    print("No Tex Beginning Match!")
else:
    print("Tex Beginning Match!")

#-------------------------------------------------------------------
# Problem 3 Instructions
#  In the quotes write the regular expression that matches the words
#  "hello" or "hero" but not "hobo" (no quotes)

x = re.search("Change Me", text)

if x == None:
    print("Problem 3 No Match")
else:
    print("Problem 3 Match")

#-------------------------------------------------------------------
# Problem 4 Instructions
#  In the quotes write the regular expression that matches the words
#  "grand" or "grind" but not "ground" (no quotes)

x = re.search("Change Me", text)

if x == None:
    print("Problem 4 No Match")
else:
    print("Problem 4 Match")


#-------------------------------------------------------------------
# Problem 5 Instructions
#  In the quotes write the regular expression that matches the words
#  "Good Day" or "Good Night" but not "Good Afternoon" (no quotes)

x = re.search("Change Me", text)

if x == None:
    print("Problem 5 No Match")
else:
    print("Problem 5 Match")


#-------------------------------------------------------------------
# Problem 6 Instructions
#  In the quotes write the regular expression that matches the string
#  of a number between 100 and 299

x = re.search("Change Me", text)

if x == None:
    print("Problem 6 No Match")
else:
    print("Problem 6 Match")



#-------------------------------------------------------------------
# Problem 7 Instructions
#  In the quotes write the regular expression that matches when
#  word with q not followed by u.  "quest" would not match but
#  qat would match

x = re.search("Change Me", text)

if x == None:
    print("Problem 7 No Match")
else:
    print("Problem 7 Match")



#-------------------------------------------------------------------
# Problem 8 Instructions
#  In the quotes write the regular expression that matches any social security
#  number.  Exactly 11 characters in the form 999-99-9999

x = re.search("Change Me", text)

if x == None:
    print("Problem 8 No Match")
else:
    print("Problem 8 Match")

    
#-------------------------------------------------------------------
# Problem 9 Instructions
#  In the quotes write the regular expression that has a dollar
#  sign $ anywhere in the string

x = re.search("Change Me", text)

if x == None:
    print("Problem 9 No Match")
else:
    print("Problem 9 Match")



#-------------------------------------------------------------------
# Problem 10 Instructions
#  In the quotes write the regular expression that matches if the 
#  string valid email address with a .com, .net or .edu domain
#  ex:  Someletters@moreLetters.com
#this one is difficult be sure to check with all of these
##text = "@.com"    #not valid
##text = "@go.edu"  #not valid
##text = "@go.net"  #not valid
##text = "a@a.a"    #not valid

x = re.search("Change Me", text)

if x == None:
    print("Problem 10 No Match")
else:
    print("Problem 10 Match")    




#-------------------------------------------------------------------
# Problem 11 Instructions
#  Use the findall function to process textVar and get a list of
#   names that begin with A.

textVar = "Bill, Amy, Jim, Andy, Susan, Manny, Alex"

s = re.findall(r"Change Me", textVar)

print(s)



#-------------------------------------------------------------------
# Problem 12 Instructions
#  Use the sub function to replace all commas with a pipe | character
#   

textVar = "Bill, Amy, Jim, Andy, Susan, Manny, Alex"

s = re.sub("Change Me", "Change Me", textVar)

print(s)


#-------------------------------------------------------------------
# Problem 13 Instructions
#  Use the findall function to process textVar and get a list of
#   names that are 4 letters or longer.

textVar = "Bill, Amy, Jim, Andy, Susan, Manny, Alex"

s = re.findall("Change Me", textVar)

print(s)




#-------------------------------------------------------------------
# Problem 14 Instructions
#  Use the sub function to replace all email addresses domains to @acme.com
#   leave the username as is

textVar = "Bill@sales.acme.com, Amy@hr.acme.com, Jim@rd.acme.com"

s = re.sub("Change Me", "Change Me", textVar)

print(s)



#-------------------------------------------------------------------
# Problem 15 Instructions
#  Use the findall function to process textVar and get all of the
#  numeric values in a list

textVar = "1001, Beloved, FIC, 12.95, Y, 5, Toni, Morrison, Plume"

s = re.findall(r"Change Me", textVar)

print(s)




