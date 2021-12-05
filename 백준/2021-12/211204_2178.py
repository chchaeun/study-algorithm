import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dq = deque()
dq.append((0, 0))
count = 1

while dq:
    x, y = dq.popleft()
    count=table[x][y]+1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if table[nx][ny]==0:
            continue
        elif table[nx][ny]==1:
            dq.append((nx, ny))
            table[nx][ny] = count
        else:
            if table[nx][ny]<=count:
                continue
            else:
                dq.append((nx,ny))
                table[nx][ny] = count
                
print(table[n-1][m-1])

