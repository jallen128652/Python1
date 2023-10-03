#*********************Built in modules notes*********************************
"""
Python has a large number of built in modules. help() will show you modules in
your python installation. 
The list that extends several pages.
You can read descriptions at: https://docs.python.org/3/py-modindex.html
Or Google search "python built in modules"
"""
#will call the help fx and let's you access information on python modules,
# keywords, etc.
#help() #un-comment to use

# to use a built in module just import
# you can read the list of fx's in a built in module on the link above
#example
import math as m
a = 5.3
b = 6.9
#pythag
# The hypotenuse is the sqrt of a^2 + b^2 or a^2 + b^2 = c^2
hypotenuse = m.sqrt(a*a + b*b)
print(hypotenuse)

#random num generator
import random as r
print(r.randint(1,10))
print(r.randint(1,10)) # prints a random int between 1 and 10

#if you use the from keyword you can import individual fx's
#example
from random import randint as r # note you can even use aliases on the fx's
print(r(1,10))
print(r(10,20))


