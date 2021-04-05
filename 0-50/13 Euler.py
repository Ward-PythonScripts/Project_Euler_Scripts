#test

def test():
    word = "54454546546544654654654654654654\n"
    word.replace("\n","")
    print(word)
#test()



# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def getNum(fileName):
    num = []
    f = open(fileName,"r")
    for l in f:
        #print(l)

        num.append(int(l.replace("\n","")))
    return num

def findSum(num):
    firstDigits = ""
    sum = 0
    for x in num:
        sum+=int(x)
    word = str(sum)
    for x in range(0,10):
        firstDigits += word[x]
    return firstDigits

print(findSum((getNum("13 Euler.txt"))))

