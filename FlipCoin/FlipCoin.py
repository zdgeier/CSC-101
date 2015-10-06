import random

def coinFlip(num):
    heads = 0
    tails = 0

    for i in range(0,num):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1

    return tails, heads

def main():
    num = eval(input("How many flips?: "))
    result = coinFlip(num)

    print(result[0])

main()