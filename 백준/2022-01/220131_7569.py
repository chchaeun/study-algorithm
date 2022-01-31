# h n m으로 접근하는 것 주의!

import sys; input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while dq:
        z, y, x = dq.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<h:
                if tomato[nz][ny][nx]==0 or tomato[nz][ny][nx]>tomato[z][y][x]+1:
                    tomato[nz][ny][nx] = tomato[z][y][x]+1
                    dq.append((nz, ny, nx))

def ans(tomato):
    answer=0
    for i in tomato: 
        for j in i:
            for k in j:
                if k==0: return -1
                answer = max(answer, k)
    return answer-1
    
dq = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                dq.append((i, j, k))
bfs()
print(ans(tomato))