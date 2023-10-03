# in module python file
pi = 3.14159265359

def larger (a, b):
    if a > b:
        return a
    return b
# can only have variables and fx's and classes in custom module files
# can create code libraries you can use in multiple programs
# put your favorite fx's and vars in them

#second fx
def calculateGrossPay(HoursWorked, PayRate):
    if HoursWorked > 40:
        BasePay = 40 * PayRate
        OverTime = (HoursWorked - 40) * PayRate
        GrossPay = BasePay + OverTime
        
    else:
        GrossPay = HoursWorked * PayRate
        
    return GrossPay


