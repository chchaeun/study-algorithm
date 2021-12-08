import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())

table=[[0 for _ in range(n)] for _ in range(m)]

# 좌표 부분이 틀렸음
# table은 뒤집혀도 똑같다. 영역 나누거나 카운트 하는 문제에서는 뒤집혀도 됨
# 왼쪽 아래 좌표가 (0.0)으로 시작해도 상관X
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            table[y][x]=1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    table[y][x]=1
    count=1
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<m and 0<=nx<n and table[ny][nx]==0:
                dq.append((ny, nx))
                table[ny][nx]=1
                count+=1
    result.append(count)

result = []
for i in range(m):
    for j in range(n):
        if table[i][j]==0:
            bfs(i, j)
        
result.sort()
print(len(result))
for r in result:
    print(r, end=" ")
    
    
# dfs recursion error
'''
def dfs(table, y, x):
    if table[y][x]==1:
        return False

    global count
    table[y][x] = 1
    count+=1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=nx<n and 0<=ny<m and table[ny][nx]==0:
            dfs(table, ny, nx)            
    return True

count=0
result = []
for i in range(m):
    for j in range(n):
        if dfs(table, i, j):
            result.append(count)
            count=0
        
result.sort()
print(len(result))
for r in result:
    print(r, end=" ")
'''