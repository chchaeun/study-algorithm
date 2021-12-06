import sys
from collections import deque

n = int(sys.stdin.readline().strip())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_height = min(map(min, table))
max_height = max(map(max, table))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(table, rain, a, b):
    global visited
    if table[a][b]<=rain or visited[a][b]==1:
        return False
    dq = deque()
    dq.append((a, b))
    visited[a][b]=1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visited[nx][ny]==0 and table[nx][ny]>rain:
                dq.append((nx, ny))
                visited[nx][ny]=1
    return True        

result= -1
for h in range(min_height-1, max_height+1):
    count=0
    rain=h
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bfs(table, rain, i, j):
                count+=1
    result = max(result, count)
    
print(result)

# 반복을 min_height부터 시작했을 때 반례
# 2
# 2 2
# 2 2
# 비가 오지 않는 경우 혹은 모든 높이보다 낮게 오는 경우 안전구역이 무조건 1개 생기는데 그 점을 고려하지 않았음.