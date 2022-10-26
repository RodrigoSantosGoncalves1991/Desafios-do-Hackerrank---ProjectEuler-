# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    factor = 1
    for k in list(range(2, n+1)):
        factor = factor * k
    return factor


def latticePaths(N, M):
    k = factorial(N+M)
    b = factorial(N)
    d = factorial(M)
    return k // (b * d)


T = int(input())

for _ in range(T):
    N, M = map(int, input().split(' '))
    result = latticePaths(N, M) % ((10 ** 9) + 7)
    print(result)
