#!/bin/python3

import sys


def biggestProductSeries(number, n, k):
    numberString = str(number)
    counterProduct = 0
    iCounter = 0
    pivot = iCounter
    product = 1
    maxProduct = 0
    for i in numberString:
        if (int(i) == 0):
            counterProduct = 0
            product = 1
            iCounter = iCounter + 1
            continue
        if (counterProduct == 0):
            pivot = iCounter
        if (counterProduct < k):
            product = product * int(i)
            counterProduct = counterProduct + 1
            if (counterProduct == k):
                if (product > maxProduct):
                    maxProduct = product
        else:
            product = product // int(numberString[pivot])
            product = product * int(i)
            pivot = pivot + 1
            if (product > maxProduct):
                maxProduct = product
        iCounter = iCounter + 1
    return maxProduct


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    result = biggestProductSeries(num, n, k)
    print(result)
