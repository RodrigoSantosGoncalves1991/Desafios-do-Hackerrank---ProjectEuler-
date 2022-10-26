#!/bin/python3

import sys


def isPrimeNumber(number):
    i = 2
    if (number == 1):
        return False
    while (i*i <= number):
        if (number % i == 0):
            return False
        i = i + 1
    return True


def multiplicity(prime, number):
    cont = 0
    while True:
        if (number % prime == 0):
            number = number // prime
            cont = cont + 1
        else:
            break
    return cont


def smallestMultiple(N):
    primes = []
    notPrimes = []
    for i in list(range(1, N+1)):
        if (isPrimeNumber(i)):
            primes.append(i)
        elif (i != 1):
            notPrimes.append(i)
    primeFactors = {}
    for i in list(range(len(primes))):
        primeFactors[primes[i]] = 1
    for keys in primeFactors:
        for notPrime in notPrimes:
            newExponent = multiplicity(keys, notPrime)
            if (newExponent > primeFactors[keys]):
                primeFactors[keys] = newExponent
    lessMultiple = 1
    for keys in primeFactors:
        lessMultiple = lessMultiple * (keys ** primeFactors[keys])
    return lessMultiple


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = smallestMultiple(n)
    print(result)
