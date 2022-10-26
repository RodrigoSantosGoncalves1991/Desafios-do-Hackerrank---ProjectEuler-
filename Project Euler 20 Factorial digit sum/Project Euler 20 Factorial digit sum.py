# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(1500)


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def factorialDigitSum(number):
    f = factorial(number)
    stringNumber = str(f)
    summation = 0
    for digit in stringNumber:
        summation = summation + int(digit)
    return summation


T = int(input())
for _ in range(T):
    number = int(input())
    result = factorialDigitSum(number)
    print(result)
