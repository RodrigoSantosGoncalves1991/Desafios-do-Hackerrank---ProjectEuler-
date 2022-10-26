#!/bin/python3

def biggestPrimeFactor(N):
    while (N > 2):
        if (N % 2 == 0):
            N = int(N / 2)
        else:
            break
    if (N == 2 or N == 5):
        return N
    else:
        nRoot = int(round(N ** 0.5))
        k = 3
        while (k <= nRoot):
            if (N % k == 0):
                N = int(N / k)
                biggestFactor = k
            else:
                k = k + 2
        if (N > 1):
            return N
        else:
            return biggestFactor


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(biggestPrimeFactor(n))
