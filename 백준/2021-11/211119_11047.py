import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

a = [int(sys.stdin.readline()) for _ in range(n)]

dq = deque()
result=0
for i in range(n-1, -1, -1):
    if k>=a[i]:
        result += k//a[i]
        k %= a[i]

print(result)    