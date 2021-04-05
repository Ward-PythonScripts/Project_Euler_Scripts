# The sum of the squares of the first ten natural numbers is, 385
#
# The square of the sum of the first ten natural numbers is, 55**2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
# .
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def SumSquareDiff(limit):
    #Sum of squares
    sumSquare = 0
    for x in range(1,limit +1):
        sumSquare += x **2
    #square of sums
    squareSum = 0
    for x in range(1,limit +1):
        squareSum += x
    squareSum = squareSum**2
    return squareSum - sumSquare
print(SumSquareDiff(100))
