
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

def powerDigitSum(exponent):
    numb = 2**exponent
    numbS = str(numb)
    sum = 0
    for digit in numbS:
        sum+=int(digit)
    return sum
print(powerDigitSum(1000))