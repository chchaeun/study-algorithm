import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
table = [input().strip() for _ in range(n)]

def bfs(b, a):
    if visited[b][a]==1:
        return False
    dq = deque([(b, a)])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if not 0<=nx<n or not 0<=ny<n:
                continue
            if table[ny][nx]==table[y][x] and visited[ny][nx]==0:
                dq.append((ny, nx))
                visited[ny][nx] = 1
    return True

result =[]

for loop in range(2):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if bfs(i, j):
                count+=1
        if loop == 0:
            table[i] = table[i].replace('R', 'G')
    result.append(count)
print(*result)