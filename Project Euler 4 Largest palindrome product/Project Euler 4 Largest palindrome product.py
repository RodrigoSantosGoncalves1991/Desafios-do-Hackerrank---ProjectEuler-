#!/bin/python3

import sys


def theNumberIsPalindrome(number):
    if (number % 11 != 0):
        return False
    inverted = str(number)[::-1]
    if (str(number) == inverted):
        return True
    else:
        return False


def threeDigitNumberProducts(arrayProducts):
    for i in list(range(100, 1000)):
        j = i
        for j in list(range(j, 1000)):
            product = i * j
            if ((product >= 101101) and (product % 10 != 0)):
                if (theNumberIsPalindrome(product)):
                    arrayProducts.append(product)
    arrayProducts.sort()
    return arrayProducts


def largestPalindromeLessThanN(arrayProducts, N):
    index = 0
    while (arrayProducts[index] < N):
        index = index + 1
        if (index == len(arrayProducts)):
            return arrayProducts[index - 1]
    return arrayProducts[index - 1]


arrayProducts = []
arrayProducts = threeDigitNumberProducts(arrayProducts)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = largestPalindromeLessThanN(arrayProducts, n)
    print(result)
