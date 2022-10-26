#!/bin/python3

import sys


def isPrimeNumber(oddNumber):
    i = 3
    while (i*i <= oddNumber):
        if (oddNumber % i == 0):
            return False
        i = i + 2
    return True


def generateNthPrime(N):
    primes = [2]
    primeAccountant = 1
    oddNumber = 3
    while (primeAccountant < N):
        if (isPrimeNumber(oddNumber)):
            primes.append(oddNumber)
            primeAccountant = primeAccountant + 1
        oddNumber = oddNumber + 2
    return primes


def nthPrimeSearch(n, primes):
    return primes[n - 1]


primes = generateNthPrime(10 ** 4)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = nthPrimeSearch(n, primes)
    print(result)
