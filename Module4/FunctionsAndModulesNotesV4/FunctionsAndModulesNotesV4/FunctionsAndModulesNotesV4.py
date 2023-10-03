#****************Lambda/Anonymous Functions**************************
#A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one
# expression.
"""
Lambda/Anonymous Functions
Anonymous functions are also called lambda functions.
An anonymous function is a function that is defined without a name.
Normal functions are defined using the def keyword
Anonymous functions are defined using the lambda keyword.
A lambda function can be assigned to a variable
"""
#Lambda functions can have any number of arguments but only one expression.
#Syntax:
	#lambda arguments: expression
#example
double = lambda x: x * 2

print(double(5))

#multiple arg example
add = lambda a, b: a + b

print(add(5, 7)) #calls the add lambda fx and passes 2 vals and prints the result

#alt with strings
caps = lambda x, y: x.upper() + " " + y.upper()

print(caps("Tony", "Lozano"))

"""
The power of lambda is better shown when you use them as an anonymous function
inside another function.
The function call is assigned to the variable times2
"""
#example
def multiplyby(p):
    return lambda x: x * p

#assigns the fx to a var while passing an arg
times2 = multiplyby(2) # p is 2
times3 = multiplyby(3)

#calls the fx and passes the inner arg
print(times2(5)) # x is 5
print(times3(5))
#this allows us to create multiple functions from just the calls