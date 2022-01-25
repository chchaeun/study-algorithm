import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
global _max
_max = 0
def dfs(x, y, count, _sum):
    global _max
    if count == 3:
        _max = max(_max, _sum)
        return
        
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
            if count == 1:
                visited[nx][ny] = 1
                dfs(x, y, count+1, _sum+board[nx][ny])
                visited[nx][ny] = 0
            
            visited[nx][ny] = 1
            dfs(nx, ny, count+1, _sum+board[nx][ny])
            visited[nx][ny] = 0
                

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, board[i][j])
        visited[i][j] = 0
        
print(_max)

# solution: https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-14500-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8