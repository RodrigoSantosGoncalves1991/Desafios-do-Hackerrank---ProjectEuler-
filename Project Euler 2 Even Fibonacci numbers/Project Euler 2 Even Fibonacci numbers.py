#!/bin/python3

import sys


def fastFibonacci(fibonacciSequence):
    tam = len(fibonacciSequence) - 1
    return fibonacciSequence[tam] + fibonacciSequence[tam - 1]


def generateFibonacciSequence(fibonacciSequence, N):
    while (True):
        fn = fastFibonacci(fibonacciSequence)
        if (fn < N):
            fibonacciSequence.append(fn)
        else:
            break
    return 1


def sumEvenTerms(fibonacciSequence, N):
    k = 2
    sum = 0
    while (True):
        fn = fibonacciSequence[k-1]
        k = k + 3
        if (fn <= N):
            sum = sum + fn
        else:
            break
    return sum


t = int(input().strip())
fibonacciSequence = [1, 2]
generateFibonacciSequence(fibonacciSequence, 4 * (10 ** 17))
for a0 in range(t):
    n = int(input().strip())
    print(sumEvenTerms(fibonacciSequence, n))
