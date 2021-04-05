#
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
primes = []

def Prime(index):
    x = 2
    amountOfPrimes = 0
    while True:
        if(isPrime(x)):
            #prime Number
            amountOfPrimes += 1
            #primes.append(x)
            #print("We found prime with value " + str(x) + " this is the " + str(amountOfPrimes) + "th primeNumber")
        if amountOfPrimes == index:
            #print(primes)
            return x
        x += 1

def isPrime(n):
    nums_to_check = range(2,int(n**.5)+1)
    for num in nums_to_check:
        if n%num == 0:
            return False
    return True

print(Prime(10001))

