from itertools import permutations
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for p in list(permutations(numbers, m)):
    print(*p)