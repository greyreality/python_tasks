# Python3 program to check if three
# sides form a  triangle or not
# У треугольника сумма любых двух сторон должна быть больше третьей.
def checkValidity(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True
# Operator	Meaning	Example
# and	True if both the operands are true	x and y
# or	True if either/ИЛИ of the operands is true	x or y
# not	True if operand is false (complements the operand)	not x

a = 3
b = 4
c = 5
if checkValidity(a, b, c):
    print("Valid")
else:
    print("Invalid")