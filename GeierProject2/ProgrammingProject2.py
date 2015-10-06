# Zachary Geier - 10/1/2015 - Programming Project 2
#
# A simple testing program
#
# Input:    Name, Social Security Number, Answers
# Output:   Correct Answers

# Returns if the Social Security Number is valid
def validSocialSecurity(num):
    result = True

    if len(num) != 11:
        result = False

    i = 0
    for c in num:
        if c == '-' and (i != 3 and i != 6):
            result = False

        i += 1

    return result

# Returns a valid SSN from the user
def getSSN():
    ssn = ''

    while not validSocialSecurity(ssn):
        ssn = input("Social Security Number: ")

    print()
    return ssn

# Gets name from user
def getName():
    return input("Name: ")

# Gets a user answer
def getUserAnswer():
    return input("Answer: ")

# Displays a question in a list
def displayQuestion(questionList, num):
    print(questionList[num])

# Displayes the correct answer to the question
def displayCorrectAnswer(key, ans, num):
    if key[num] == ans:
        print("That's Correct!\n")
    else:
        print("Sorry the answer is", key[num], '\n')

# Returns if the value is "Correct" or "Wrong"
def checkMatch(correct, val):
    if correct == val:
        result = "Correct"
    else:
        result = "Wrong"

    return result

# Displays all results
def displayEndOutput(name, ssn, key, userKey):
    numWrong = 0

    # Prints output header
    print()
    print(format(name + "Test Results", '^40s'))
    print(format("Social Security #: " + ssn, '^40s'))
    print()

    # Prints table header
    print(format("Question", '15s'),
          format("Result", '15s'),
          format("Correct Answer", '15s'))

    # Prints question number, user answer, and correct answer
    for i in range(4):
        if checkMatch(key[i], userKey[i]) == "Correct":
            answer = "Correct"
            answerVal = ''
        else:
            answer = "Wrong"
            answerVal = key[i]
            numWrong += 1

        print(format(str(i + 1), '15s'),
              format(answer, '15s'),
              format(answerVal, '15s'))

    # Calculates and prints percent right
    percent = format(((len(key) - numWrong) / len(key)) * 100, '3.0f')

    print("\nTest Score:", str(percent) + '%')

def main():
    key = ['A', 'B', 'C', 'D']
    userKey = []

    # All possible questions and answers
    questions = ["What does type(type) equal?:\n\tA) Type\n\tB) Int\n\tC) String\n\tD) String",
                 "What is the first letter of the alphabet?:\n\tA) B\n\tB) A\n\tC) D\n\tD) C",
                 "When was Python created?:\n\tA) 2000\n\tB) 1990\n\tC) 1989\n\tD) 4",
                 "How many feels does Mr. Howard have?:\n\tA) 1\n\tB) 9000\n\tC) 4\n\tD) 0"]

    # Gets name and Social Security number from the user
    name = getName()
    ssn = getSSN()

    # Displays each question, gets user answer, and displays the correct answer
    for i in range(4):
        displayQuestion(questions, i)
        userKey.append(getUserAnswer())
        displayCorrectAnswer(key, userKey[i], i)

    # Displays all output information
    displayEndOutput(name, ssn, key, userKey)


main()