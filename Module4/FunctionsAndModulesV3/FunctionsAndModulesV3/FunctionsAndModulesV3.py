#**********************Function Return Values*****************************
#***************Return values**************
# You can have a function return a value or values by providing a return
# statement
#example
def add(num1, num2):
    return(num1 + num2)
n = add(4, 6) #n because we need a place to store the return values
print(n)

#example2
#checking from prime numbers or numbers that are only divisible by 1 and itself
#brute force is prime
def isNumPrime(val):
    i = 2
    if val < 2: #0, 1 will be marked prime by the algo
        return False
    while i * i <= val: # we'll know if val is prime by the time we reach the sqrt of val
        if (val % i == 0):
            return False
        i += 1
    return True
# the loop tests all numbers from 1 to 100 to see if they are prime
count = 0
for x in range(1, 100):
    if isNumPrime(x):
        print(x)
        count += 1
#prints the amount of prime numbers in the range excluding 0 and 1
print(count)

#************Multiple return values**************
#You can return multiple values with return
#A tuple is returned, that you can also unpack (strange syntax)
#example
def mult_ret():
    return 5, 10
x = mult_ret() #tuple
print(x)
y, z = mult_ret() #unpacking the tuple by assigning the vals to vars
print(y, z)
