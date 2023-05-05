# Operators
# Arithmetic operators
# +-*/% ** //
# +
print(10 + 20)  # addition
print(20 - 10)  # subtraction
print(10 * 2)  # multiplication
print(10 / 2)  # 5 #divison
print(11 % 2)  # 1 remainder
print(10 ** 2)  # 10*10
print(10 ** 3)  # 10 *10*10 exponential
print(1456 // 10)  # 145  floor division

print("///Assignment /////")
# Assignment operator
x = 10  # equal operator
x += 2  # it's nothing but x = x+2
print(x)
x -= 3  # x = x-3
x *= 4  # x = x*4
x /= 5  # x = x/5
x %= 3  # x = x%5
x //= 10  # x = x// 10
x **= 10  # x = x ** 10

print("////comparison operator")
# comparison operator
x = 10
y = 10
print(x == y)  # True
10 != 9  # True
10 > 9  # True
10 < 9  # False
10 >= 10  # True
9 <= 10  # True

print("///////Logical operator////")
# Logical operators
# and ,or , not
#  and => this and that => both conditions should match
#  or => this or that => any one condition should match
# not => True will become false , False will become True
x = 5
print("//and//")
print(x > 4 and x < 10)  # True and True  => True
print(x > 4 and x > 11)  # True and False  => False
print(x > 6 and x < 10)  # False and True  => False
print(x > 6 and x > 11)  # False and False => False
print("//or//")
print(x > 4 or x < 10)  # True and True  => True
print(x > 4 or x > 11)  # True and False  => True
print(x > 6 or x < 10)  # False and True  => True
print(x > 6 or x > 11)  # False and False => False
print("//not//")
print(not (x > 4 or x < 10))  # True will become False because of not  => False

print("/////Identity operator//")
# Identity Operator
# it will check whether both objects are same or not
# whether both variables are linked
x = 10
y = 10.0
l1 = [1, 2, 4]
print(type(l1) is list)
print(x is y)
print(x is not y)

print("///////Membership operator//")
# Membership operator
# in => checks values is there inside
l1 = [1, 2, 5, 6, 7]
print(4 in l1)  # False
print(2 in l1)  # True
print(2 not in l1)  # False

