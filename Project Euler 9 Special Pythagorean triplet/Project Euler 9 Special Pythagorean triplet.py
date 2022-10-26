#!/bin/python3

import sys


def pythagoreanTriplet(N):
    products = -1
    if (N % 2 != 0):
        return -1
    for a in list(range(1, N//3)):
        b = (N*N - 2 * a * N) // (2 * N - 2 * a)
        c = N - a - b
        if (a*a + b*b == c*c):
            if (a*b*c > products):
                products = a*b*c
    return products


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(pythagoreanTriplet(n))
