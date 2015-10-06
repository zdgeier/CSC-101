i = 1
funct = 0

while i <= 100000:
    funct += ((-1)**(i + 1)) / (2 * i - 1)

    if i % 10000 == 0:
        pi = 4 * funct
        print(pi)

    i += 1
