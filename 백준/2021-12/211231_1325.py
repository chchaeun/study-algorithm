import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())

table = defaultdict(list)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    table[b].append(a)

def bfs(i):
    count=0
    visited = [False] * (n+1)
    visited[i]=True
    dq = deque([i])
    while dq:
        v = dq.popleft()
        for k in table[v]:
            if not visited[k]:
                visited[k] = True
                count+=1
                dq.append(k)
    return count

max_count = -1
result = []

for i in range(1, n+1):
    temp = bfs(i)
    if max_count < temp:
        result = [i]
        max_count = temp
    elif max_count == temp:
        result.append(i)

for i in result:
    print(i, end=" ")