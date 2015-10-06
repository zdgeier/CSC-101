#IP4 to binary

x1 = eval(input("Enter the first octet of an IP4 address: "))

x2 = eval(input("Enter the second octet of an IP4 address: "))

x3 = eval(input("Enter the third octet of an IP4 address: "))

x4 = eval(input("Enter the fourth octet of an IP4 address: "))

y01 = x1 % 2
x1 //= 2
y02 = x1 % 2
x1 //= 2
y03 = x1% 2
x1 //= 2
y04 = x1% 2
x1 //= 2
y05 = x1% 2
x1 //= 2
y06 = x1% 2
x1 //= 2
y07 = x1% 2
x1 //= 2
y08 = x1% 2
x1 //= 2

z1 = str(y08) + str(y07) + str(y06) + str(y05) + str(y04) + str(y03) + str(y02) + str(y01) 

y11 = x2 % 2
x2 //= 2
y12 = x2 % 2
x2 //= 2
y13 = x2% 2
x2 //= 2
y14 = x2% 2
x2 //= 2
y15 = x2% 2
x2 //= 2
y16 = x2% 2
x2 //= 2
y17 = x2% 2
x2 //= 2
y18 = x2% 2
x2 //= 2

z2 = str(y18) + str(y17) + str(y16) + str(y15) + str(y14) + str(y13) + str(y12) + str(y11) 

y21 = x3 % 2
x3 //= 2
y22 = x3 % 2
x3 //= 2
y23 = x3% 2
x3 //= 2
y24 = x3% 2
x3 //= 2
y25 = x3% 2
x3 //= 2
y26 = x3% 2
x3 //= 2
y27 = x3% 2
x3 //= 2
y28 = x3% 2
x3 //= 2

z3 = str(y28) + str(y27) + str(y26) + str(y25) + str(y24) + str(y23) + str(y22) + str(y21) 

y31 = x4 % 2
x4 //= 2
y32 = x4 % 2
x4 //= 2
y33 = x4% 2
x4 //= 2
y34 = x4% 2
x4 //= 2
y35 = x4% 2
x4 //= 2
y36 = x4% 2
x4 //= 2
y37 = x4% 2
x4 //= 2
y38 = x4% 2
x4 //= 2

z4 = str(y38) + str(y37) + str(y36) + str(y35) + str(y34) + str(y33) + str(y32) + str(y31) 

print(z1, z2, z3, z4, sep=".")

