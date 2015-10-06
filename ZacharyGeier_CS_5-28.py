e = 1
item = 1

i = 1
while i < 100:
    
    j = 0
    while i > j:
        item *= i - j

        j += 1

    e += 1 / item
    
    if i % 10 == 0:
        print(e)

    i += 1
