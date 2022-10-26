# Enter your code here. Read input from STDIN. Print output to STDOUT

def nameScore(string, names_in_order):
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
                'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    score = 0
    for char in string:
        score += alphabet[char]
    return score * (names_in_order.index(string) + 1)


N = int(input())

names = []
for _ in range(N):
    names.append(input())

names_in_order = sorted(names)

Q = int(input())

for _ in range(Q):
    name = input()
    result = nameScore(name, names_in_order)
    print(result)
