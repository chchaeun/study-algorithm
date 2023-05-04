from itertools import combinations
n, m = map(int, input().split())
numbers = [i+1 for i in range(n)]

for p in list(combinations(numbers, m)):
    print(*p)