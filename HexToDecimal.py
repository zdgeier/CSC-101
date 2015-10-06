#Hex to Decimal

x = input("Enter a four digit hexadecimal number: ")

x1 = (ord(x[0]) - 48) * 16**3
x2 = (ord(x[1]) - 48) * 16**2
x3 = (ord(x[2]) - 48) * 16**1
x4 = (ord(x[3]) - 48) * 16**0

print(ord('a'))
print(ord('9'))
print(x1, x2, x3, x4)
