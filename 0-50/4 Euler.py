
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def FindPalinDrome(amountOfDigits):
    palindromes = []
    for x in range(1,10**amountOfDigits):
        for y in range(1,10**amountOfDigits):
            number = str(x*y)
            #print(number)
            if number == number[::-1]:
                palindromes.append(x*y)
    palindromes.sort()
    #print(palindromes)
    return palindromes[-1]

print(FindPalinDrome(3))
