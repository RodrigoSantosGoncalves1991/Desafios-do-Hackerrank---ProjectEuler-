
T = int(input())
numbers = []
for _ in range(T):
    numbers.append(int(input()))

result = str(sum(numbers))
print(result[0:10])
