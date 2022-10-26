# Enter your code here. Read input from STDIN. Print output to STDOUT


def MaximumPathSum(t):
    i = len(t) - 2
    while i >= 0:
        j = 0
        while j < len(t[i]):
            t[i][j] += max(t[i + 1][j], t[i + 1][j + 1])
            j += 1
        i -= 1
    return t[0][0]


T = int(input())

for _ in range(T):
    N = int(input())
    triangle = []
    for _ in range(N):
        triangle.append(list(map(int, input().split(' '))))
    result = MaximumPathSum(triangle)
    print(result)
