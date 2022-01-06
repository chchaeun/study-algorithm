import sys

input = sys.stdin.readline

r, c = map(int, input().split())

table = [list(map(lambda x: ord(x)-65, input().strip())) for _ in range(r)]

alpha = [0] * 26

result = 0 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, count):
    global result
    result = max(count, result)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and alpha[table[nx][ny]]== 0:
            alpha[table[nx][ny]]=1
            dfs(nx, ny, count+1)
            alpha[table[nx][ny]]=0
    
alpha[table[0][0]]=1
dfs(0, 0, 1)
print(result)