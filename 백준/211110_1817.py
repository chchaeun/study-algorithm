import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

dq = deque()

if n==0:
    print("0")
else:
    weight = list(map(int, sys.stdin.readline().split()))
    dq.append(weight[0])    
    for i in range(1, n):
        top = len(dq)-1
        temp = dq[top]+weight[i]
        if temp > m:
            dq.append(weight[i])
        else:
            dq[top] += weight[i]
    print(len(dq))