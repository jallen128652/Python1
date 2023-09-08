#***********************NOTES FOR M1 LESSON3*********************
#************************OPERATORS**************************
#arithmetic operators
#Arithmetic operators are used with numeric values to perform common mathematical
# operations:
#**Note: some of these operators have different fx's when used with non-numeric operands
# such as the + operator with strings
"""
Operator	Name				Example	
+			Addition			x + y	
-			Subtraction			x - y	
*			Multiplication		x * y	
/			Division			x / y	
%			Modulus				x % y	
**			Exponentiation		x ** y	
//			Floor division		x // y	(integer round down)
@			at
"""

#assignment operators
#Assignment operators are used to assign values to variables:
"""
Operator	Example		Same As	
=			x = 5		x = 5	
+=			x += 3		x = x + 3	
-=			x -= 3		x = x - 3	
*=			x *= 3		x = x * 3	
/=			x /= 3		x = x / 3	
%=			x %= 3		x = x % 3	
//=			x //= 3		x = x // 3	
**=			x **= 3		x = x ** 3	
&=			x &= 3		x = x & 3	
|=			x |= 3		x = x | 3	
^=			x ^= 3		x = x ^ 3	
>>=			x >>= 3		x = x >> 3	
<<=			x <<= 3		x = x << 3
"""
#example
a = 2
b = 3
c = (a*a + b*b)**0.5
#	(2*2 + 3*3)^0.5
print(c)

#order of operations for operators
# items that have the same precedence are performed left to right
"""
Operator				Description	
()						Parentheses	
**						Exponentiation	
+x  -x  ~x				Unary plus, unary minus, and bitwise NOT	
*  /  //  %	 @			Multiplication, division, floor division, modulus and at	
+  -					Addition and subtraction	
<<  >>					Bitwise left and right shifts	
&						Bitwise AND	
^						Bitwise XOR	
|						Bitwise OR	
==  !=  >  >=  <  <=	Comparisons, identity, and membership operators
is  is not  in  not in 		
not						Logical NOT	
and						AND	
or						OR
"""

#***************INPUT FUNCTION AND INPUT***************************

