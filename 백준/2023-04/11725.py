import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
node = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

visited = [False for _ in range(n+1)]
dq = deque([1])

while dq:
    d = dq.popleft()
    visited[d] = True

    for i in node[d]:
        if not visited[i]:
            parents[i] = d
            dq.append(i)

for p in parents[2:]:
    print(p)