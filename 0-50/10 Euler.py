#
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def SummationOfPrimes(limit):
    sum = 0
    for x in range(2,limit +1):
        if isPrime(x):
            sum += x
    return sum


def isPrime(n):
    nums_to_check = range(2,int(n**0.5 +1))
    for num in nums_to_check:
        if n%num == 0:
            return False
    #print(n)
    return True
print(SummationOfPrimes(2*10**6))