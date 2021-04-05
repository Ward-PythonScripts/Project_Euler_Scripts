#
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2 2's zijn machten
#
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

def findTriplet(sumOfABC):
    #Find all pythogorean triplets < 1000
    for a in range(1,sumOfABC):
        for b in range(1,sumOfABC):
            c = math.sqrt(a**2 + b**2)
            if c%1 == 0 and a+b+c == sumOfABC:
                print("Value of a: " + str(a) + ", value of b: " + str(b) + ", value of c: " + str(c))
                return a*b*c
print(findTriplet(1000))
