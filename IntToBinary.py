#Integer to binary

x = eval(input("Enter a positive integer no larger than 255: "))

y1 = x % 2
x //= 2
y2 = x % 2
x //= 2
y3 = x % 2
x //= 2
y4 = x % 2
x //= 2
y5 = x % 2
x //= 2
y6 = x % 2
x //= 2
y7 = x % 2
x //= 2
y8 = x % 2
x //= 2


print(y8, y7, y6, y5, y4, y3, y2, y1, sep='')
