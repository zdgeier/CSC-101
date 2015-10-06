#Binary to Octal

x = input("Enter a 9 bit binary number: ")

x1 = int(x[0]) * 4
x2 = int(x[1]) * 2
x3 = int(x[2])
x4 = int(x[3]) * 4
x5 = int(x[4]) * 2
x6 = int(x[5])
x7 = int(x[6]) * 4
x8 = int(x[7]) * 2
x9 = int(x[8])

y1 = x1 + x2 + x3
y2 = x4 + x5 + x6
y3 = x7 + x8 + x9

print(y1, y2, y3, sep='')


        
