#!/bin/python3

import sys


def sumSquareDifference(N):
    return ((N*(N+1)) // 2) ** 2 - (N*(N+1)*(2*N+1)) // 6


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = sumSquareDifference(n)
    print(result)
