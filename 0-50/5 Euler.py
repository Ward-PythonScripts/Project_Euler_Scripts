#
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import itertools

def smallestMultiple(limit):
    x= limit
    index = 0
    hits = 1
    #limiter
    limiter = 1
    for x in range(1,limit+1):
        limiter = limiter*x
    #limiter
    while True:
        isDivisble = True
        for y in range(1,limit+1):
            if not x%y == 0:
                isDivisble = False
                break
        if isDivisble:
            return x
        if index >= 10000000:

            print("We are now at the " + str(index*hits) + " mark")
            hits += 1
            index = 0
        index += 1
        x += limit

        #limiter
        if x>limiter:
            return 0

print(smallestMultiple(20))