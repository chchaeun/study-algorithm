from multiprocessing.connection import answer_challenge
import sys; input=sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
global answer
answer = -1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False]*m for _ in range(n)]

def dfs(x, y, _sum, count):
    global answer
    if count == 3:
        answer = max(answer, _sum)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, _sum+board[nx][ny], count+1)
            visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

print(answer)        