
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatzChain(limit):
    longestChain = 0
    longestN = 0
    dictionarry = [[0,0]]
    for x in range(round(limit*0.5),limit +1):
        length = 1
        n = x

        while n!= 1:
            #print(n)
            if n in dictionarry[0]:
                length += dictionarry[1]
                n=1
                break
            else:
                if n%2 == 0:
                    n = int(n/2)
                else:
                    n = int(3*n+1)
                length += 1
        if longestChain < length:
            longestChain = length
            longestN = x
        dictionarry.append([x,length])
        if x%100000 == 0:
            print(str(longestChain) + " is the longest chain with n is " + str(x))
            #print(int(n))
    print(longestN)
    return longestChain
print(collatzChain(10**6))
