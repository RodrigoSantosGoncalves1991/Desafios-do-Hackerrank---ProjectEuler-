# Enter your code here. Read input from STDIN. Print output to STDOUT

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
    primes = dict(filter(lambda prime: prime[1] == True, primes.items()))
    return primes


def multiplicity(prime, n):
    counter = 0
    while True:
        if (n % prime == 0):
            n = n // prime
            counter += 1
        else:
            return counter, n


def _numberOfDividers(n, primes):
    numberOfDividers = 1
    #testNumber = 1
    for prime in primes:
        exponent, n = multiplicity(prime, n)
        if (exponent > 0):
            numberOfDividers = numberOfDividers * (exponent + 1)
            #testNumber = testNumber * (prime ** exponent)
        if (n == 1):
            break
    return numberOfDividers


def moreThanNdividers(N, initial_k, primes):
    k = initial_k
    while True:
        triangularNumber = ((1 + k) * k) // 2
        numberOfDividers = _numberOfDividers(triangularNumber, primes)
        if (numberOfDividers > N):
            return triangularNumber, k, numberOfDividers
        k += 1


def highlyCompositeTriangularNumbers(N, primes):
    dividers = 1
    initial_k = 1
    triangularNumbers = dict()
    while (dividers <= N):
        triangularNumber, initial_k, _dividers = moreThanNdividers(
            dividers, initial_k, primes)
        triangularNumbers[triangularNumber] = _dividers
        dividers = 1 + _dividers
    return triangularNumbers


def searchTriangularNumbers(triangularNumbers, N):
    for triangularNumber in triangularNumbers:
        if (triangularNumbers[triangularNumber] > N):
            return triangularNumber


primes = generateNthPrime(50)
triangularNumbers = highlyCompositeTriangularNumbers(1000, primes)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = searchTriangularNumbers(triangularNumbers, n)
    print(result)
