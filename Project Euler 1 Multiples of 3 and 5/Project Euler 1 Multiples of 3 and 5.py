#!/bin/python3

import sys


def sumOfMultiplesPer_PA(n, r):
    n = n - 1
    a_n = 0
    while (True):
        if (n % r == 0):
            a_n = n
            break
        n -= 1
    if (a_n >= r):
        summ = ((a_n ** 2) + r * a_n)//(2 * r)
        return int(summ)

    else:
        return 0


def sumOfMultiples3And5(n):
    return sumOfMultiplesPer_PA(n, 3) + sumOfMultiplesPer_PA(n, 5) - sumOfMultiplesPer_PA(n, 15)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = sumOfMultiples3And5(n)
    print(result)
