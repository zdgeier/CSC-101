#Zachary Geier - Hangman - 10.29

import random

#Checks if userWord has no *
def checkDone(array):
    result = True
    for i in array:
        if i == '*':
            result = False
    return result

#Generates a string from an array of characters
def genStr(array):
    string = ''
    for c in array:
        string += c
    return string

#Generates array of *'s
def genAstrikArray(word):
    array = []
    for i in range(0, len(word)):
        if word[i] == ' ':
            array.append(' ')
        else:
            array.append('*')

    return array

#Replaces the * with the letter if the letter is in the word
def findLetter(word, letter, userWord):
        letterFound = False

        for i in range(0, len(word)):
            if letter == word[i]:
                letterFound = True

                #Checks if letter has already been used
                if userWord[i] == '*':
                    userWord[i] = letter
                else:
                    print('\t', letter, "is already in the word")
                    break

        return letterFound


def main():
    words = ["python", "java", "ruby", "perl", "c++", "erlang", "pascal", "fortran", "hypertext markup language"]
    userWord = []
    missed = 0

    #Chooses a random word from 'words' array
    word = words[random.randint(0,len(words) - 1)]

    #Generates a string of *
    userWord = genAstrikArray(word)

    while checkDone(userWord) != True:
        letter = input("(Guess) Enter a letter in word " + genStr(userWord) + ' > ')

        letterFound = False

        if findLetter(word, letter, userWord) == False:
            print("\t", letter, "is not in the word. Try again.")
            missed += 1

    #Prints when program is over
    print("The word was", word, "You misssed", missed, "times.")

main()