import sys
n = int(input())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
result=0
for i in range(n):
    a_pop = a.pop(a.index(min(a)))
    b_pop = b.pop(b.index(max(b)))
    result += a_pop * b_pop
print(result)