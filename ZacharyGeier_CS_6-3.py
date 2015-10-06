#Palindrome integer - Zachary Geier

#Return the reversal of an integer
def reverse(number):
    string = str(number)
    result = ''

    for i in range(len(string) - 1, -1, -1):
        result += string[i]

    return eval(result)

#Return true if number is palindrome
def isPalindrome(number):
    if number == reverse(number):
        return True
    return False


num = eval(input('Enter an integer: '))

if isPalindrome(num) == True:
    print(num, 'is a palindrome!')
else:
    print(num, 'is not a palindrome.')
