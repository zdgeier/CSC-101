#Prime Number Generator - Zachary Geier

# Checks whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False # number is not prime
        divisor += 1

    return True # number is prime

primeQuant = 0

for i in range(2, 10001):
    if isPrime(i):
        primeQuant += 1

print('There are', primeQuant, 'prime numbers less than 10,000')
