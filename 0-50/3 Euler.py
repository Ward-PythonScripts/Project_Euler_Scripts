#
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import itertools
import time

def PrimeFactor(numb):
    time1 = time.time()
    primeNumbs = [1,2,3,5]
    combinations = []
    failedCombinations = []
    factors = []
    cNumb = numb
    #factorizatie
    primeFactorNotFound = True
    while primeFactorNotFound:
        for L in range(0,len(primeNumbs)):
            allCombinations = itertools.combinations(primeNumbs,L)
            for comb in allCombinations:
                if not comb in failedCombinations:
                    combinations.append(comb)
        for c in combinations:
            y=1
            for number in c:
                y=y*number
            if y == numb:
                print("It took " + str((time.time()-time1)*1000) + " miliseconds")
                return c

        failedCombinations.append(c)
        getNextPrime(primeNumbs,numb)



def getNextPrime(primeNumbs,numb):
    primeNotFound = True
    prime = primeNumbs[-1] +1
    while primeNotFound:
        if (not (prime %2 == 0 or prime%3 == 0 or prime%5==0)) and numb%prime == 0:
            primeNumbs.append(prime)
            primeNotFound = False
            print("Current primeNumbs are now : " + str(primeNumbs))
            return primeNumbs
        else:
            prime +=1







print(PrimeFactor(600851475143))