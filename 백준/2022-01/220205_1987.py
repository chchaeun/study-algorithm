import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

table = [list(input().strip()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        table[i][j] = ord(table[i][j])-65

# def bfs():
#     dq = deque([(0, 0)])
#     count = [[0 for _ in range(c)] for _ in range(r)]
#     count[0][0] = 1
    
#     visited = [0 for _ in range(26)]
#     first = table[0][0]
#     visited[first] = 1
    
#     _max = 0
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
    
#     while dq:
#         x, y = dq.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if not 0<=nx<r or not 0<=ny<c:
#                 continue
#             temp = table[nx][ny]
#             if visited[temp]==0:
#                 count[nx][ny] = count[x][y] + 1
#                 _max = max(count[nx][ny], _max)
#                 visited[temp]=1
#                 dq.append((nx, ny))
#     print(count)
#     return _max

# result = bfs()

# 스택 X

visited = [[False for _ in range(c)] for _ in range(r)]
alpha = [False for _ in range(26)]

result = 0

def dfs(x, y, visited, alpha):
    global result
    visited[x][y] = True
    alpha[table[x][y]] = True
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not 0<=nx<r or not 0<=ny<c:
            continue
        if visited[nx][ny] == False and alpha[table[nx][ny]] == False:
            dfs(nx, ny, visited, alpha)
    
    
dfs(0, 0, visited, alpha)
print(visited)