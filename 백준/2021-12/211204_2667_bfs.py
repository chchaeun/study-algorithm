import sys
from collections import deque
n = int(sys.stdin.readline().strip())

table = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(table, a, b):
    queue = deque()
    queue.append((a, b))
    table[a][b] = 0
    count= 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if table[nx][ny]==1:
                table[nx][ny] = 0
                queue.append((nx, ny))
                count+=1
    return count

block = []

for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            block.append(bfs(table, i, j))

block.sort()
print(len(block))
for b in block:
    print(b)

    
    