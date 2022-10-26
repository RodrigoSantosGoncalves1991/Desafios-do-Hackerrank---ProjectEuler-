#!/bin/python3

import sys


def generateNthPrime(N):
    primes = dict()
    primes[2] = True
    for i in list(range(3, N + 1, 2)):
        primes[i] = True
    i = 3
    while (i * i < N):
        p = i * i
        while (p <= N):
            primes[p] = False
            p = p + 2 * i
        i = i + 2
    return primes


def primesOfTheRange(inferior, superior, primes):
    primesRange = []
    if (superior < 2 or inferior > superior):
        return primesRange
    elif (inferior <= 2):
        inferior = 2
        primesRange.append(2)
    if (inferior % 2 == 0):
        inferior = inferior + 1
    if (superior % 2 == 0):
        superior = superior - 1
    for i in list(range(inferior, superior + 1, 2)):
        if (primes[i]):
            primesRange.append(i)
    return primesRange


def generateNthPrimeSum(N):
    sums = dict()
    sums[0] = 0
    for i in list(range(1, N+1)):
        sums[i] = sums[i-1] + sum(primesOfTheRange(i, i, primes))
    return sums


t = int(input().strip())
Numbers = []
for a0 in range(t):
    n = int(input().strip())
    Numbers.append(n)

primes = generateNthPrime(max(Numbers))
sumsPrimes = generateNthPrimeSum(max(Numbers))

for N in Numbers:
    result = sumsPrimes[N]
    print(result)
