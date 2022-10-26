# Enter your code here. Read input from STDIN. Print output to STDOUT

def collatzFunction(n, collatzSequence, tablecollatzDistance):
    collatzSequence.append(n)
    while True:
        if (n < len(tablecollatzDistance) - 1):
            if (tablecollatzDistance[n] != -1):
                collatzSequence.reverse()
                return 1
        if (n == 1):
            collatzSequence.reverse()
            return 1
        if (n & 1):
            n = 3 * n + 1
        else:
            n = n // 2
        collatzSequence.append(n)


def generateDistanceTable(N, tablecollatzDistance):
    longestChain = [0] * (N + 1)
    maxIndice = 0
    maxDistance = 0
    for k in list(range(1, N + 1)):
        if (tablecollatzDistance[k] == -1):
            collatzSequence = []
            collatzFunction(k, collatzSequence, tablecollatzDistance)
            if (collatzSequence[0] == 1):
                tablecollatzDistance[k] = len(collatzSequence) - 1
            else:
                previousDistance = collatzSequence[0]
                collatzSequence.remove(previousDistance)
                increment = 1
                for kAtual in collatzSequence:
                    if (kAtual < len(tablecollatzDistance) - 1):
                        tablecollatzDistance[kAtual] = tablecollatzDistance[previousDistance] + increment
                    increment = increment + 1
        if (tablecollatzDistance[k] >= maxDistance):
            maxDistance = tablecollatzDistance[k]
            maxIndice = k
        longestChain[k] = maxIndice
    return longestChain


t = int(input().strip())
arrayN = []
for a0 in range(t):
    n = int(input().strip())
    arrayN.append(n)


tablecollatzDistance = [-1] * (max(arrayN) + 1)
longestChain = generateDistanceTable(max(arrayN), tablecollatzDistance)

for N in arrayN:
    result = longestChain[N]
    print(result)
