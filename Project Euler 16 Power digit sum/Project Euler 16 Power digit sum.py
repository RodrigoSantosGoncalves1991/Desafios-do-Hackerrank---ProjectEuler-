# Enter your code here. Read input from STDIN. Print output to STDOUT

def powerDigitSum(N):
    number = str(2 ** N)
    sum = 0
    for k in number:
        sum = sum + int(k)
    return sum


T = int(input())
for _ in range(T):
    number = int(input())
    result = powerDigitSum(number)
    print(result)
