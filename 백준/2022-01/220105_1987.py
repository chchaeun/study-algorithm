# DFS (시간초과)

# import sys

# input = sys.stdin.readline

# r, c = map(int, input().split())

# table = [list(map(lambda x: ord(x)-65, input().strip())) for _ in range(r)]
# visited = [[0 for _ in range(c)] for _ in range(r)]
# alpha = [0] * 26

# result = 0 

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# def dfs(x, y, count):
#     global result
#     result = max(count, result)
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<r and 0<=ny<c and visited[nx][ny] == 0 and alpha[table[nx][ny]]== 0:
#             alpha[table[nx][ny]]=1
#             visited[nx][ny] = 1
#             dfs(nx, ny, count+1)
#             alpha[table[nx][ny]]=0
#             visited[nx][ny] = 0
            
    
# alpha[table[0][0]]=1
# visited[0][0] = 1
# dfs(0, 0, 1)
# print(result)


# BFS

import sys

input = sys.stdin.readline

r, c = map(int, input().split())

table = [list(input().strip()) for _ in range(r)]
result = 1 

def bfs():
    global result
    
    # 방문한 순서대로 문자열 만들어서 case로 분류
    q = set([(0, 0, table[0][0])])
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while q:
        x, y, pop_str = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and table[nx][ny] not in pop_str:
                new_str = pop_str + table[nx][ny]
                q.add((nx, ny, new_str))
                result = max(result, len(new_str))               
bfs()
print(result)