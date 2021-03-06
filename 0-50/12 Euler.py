

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

def getTriangleNumber(limit):
    triangleNumber =0
    x = 1
    visualizerCounter = 0
    hit = 0
    divisors = 999999999999


    while True:
        triangleNumber += x

        #factors = []


        divisors = 0
        for n in range(1,round(round(triangleNumber**0.5)+1)):
            if triangleNumber%n ==0:
                #factors.append(n)
                divisors += 2
        if divisors>limit:
            return triangleNumber
        x +=1

        #visualizer

        if(visualizerCounter >= 1000):
            hit += 1
            visualizerCounter = 0
            #print("We have gone for " + str(hit*1000) + " and have reached " + str(divisors) + " divisors")
        visualizerCounter += 1
        #print(str(triangleNumber) + " with factors: " + str(factors))

print(getTriangleNumber(500))