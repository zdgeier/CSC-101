import random
import os.path

def main():
    filename = input("Enter a filename: ")

    # Checks if file already exists
    while os.path.isfile(filename):
        print("File already exists!")
        filename = input("Enter a filename: ")

    # Creates file and writes 100 random numbers from 0 to 50
    file_w = open(filename, 'w')
    for i in range(100):
        file_w.write(str(random.randint(0,50)) + " ")
    file_w.close()

    # Gets text from file, stores in s
    file_r = open(filename, 'r')
    s = file_r.read()
    file_r.close()

    # Creates array of separate numbers
    numbers = [eval(x) for x in s.split()]

    # Sorts number arrray
    for i in range(len(numbers)):
        for j in range(len(numbers)-1-i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

    # Prints every number in numbers array
    for number in numbers:
        print(number, end = " ")



main()
