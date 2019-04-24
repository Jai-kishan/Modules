#here I am call a arithmetic_operators form ArithmeticOperators dircetory and after that (mul) funchtion
#which is define arithmetic_operators()
from ArithmeticOperators.arithmetic_operators import mul #if you want to use arithmetic_operators of all function() so you can replace (mul) to (*)
first_value = int(input("Enter first number : "))
second_value = int(input("Enter second number : "))
#if you want to perform any other operation then replace (mul) and put hte function name which you want to perform 
result = mul(first_value,second_value)
print(result)