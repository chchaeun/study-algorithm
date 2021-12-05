import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())

table = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    table[a].append(b)
    table[b].append(a)

for t in table:
    t.sort()    

def dfs(table, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in table[v]:
        if not visited[i]:
            dfs(table, i, visited)
            

visited = [False] * (n+1)
dfs(table, v, visited)
print()

def bfs(table, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in table[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
visited = [False] * (n+1)    
bfs(table, v, visited)