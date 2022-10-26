# Enter your code here. Read input from STDIN. Print output to STDOUT

def d(n):
    N = n
    k = 2
    summation = 1
    while k * k <= N:
        p_k = 1
        partialSum = 1
        while n % k == 0:
            n = n//k
            p_k = p_k * k
            partialSum += p_k
        summation = summation * partialSum
        k += 1
    if n > 2:
        summation = summation * (1 + n)
    return summation - N


def amicableNumbers(a, b):
    if (d(a) == b) and (d(b) == a) and a != b:
        return True
    return False


def generatingFriendlyNumbers():
    friendlyNumbers = []
    n = 1
    while n <= 10 ** 5:
        d_n = d(n)
        if d_n > 0 and n > 0:
            if amicableNumbers(n, d_n):
                friendlyNumbers.extend([n, d_n])
        n += 1
    friendlyNumbers = sorted(list(set(friendlyNumbers)))
    return friendlyNumbers


def sumOfFriendliesLessThanN(N, friendlyNumbers):
    numbersLessThanN = filter(lambda n: n < N, friendlyNumbers)
    return sum(numbersLessThanN)


friendlyNumbers = generatingFriendlyNumbers()

T = int(input())

for _ in range(T):
    N = int(input())
    result = sumOfFriendliesLessThanN(N, friendlyNumbers)
    print(result)
