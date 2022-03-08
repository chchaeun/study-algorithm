import sys; input=sys.stdin.readline
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1 for _ in range(n)] for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x==m-1 and y == n-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and board[nx][ny]<board[x][y]:
            visited[x][y] += dfs(nx, ny)
    return visited[x][y]        

print(dfs(0, 0))

# visited에 경우의 수를 표시한다.
# 처음 마지막 좌표에 도달하는 경로까지는 0으로 표시가 되다가, 마지막 좌표에 도달해서 1이 리턴되면 이전의 좌표들로 돌아오는 과정에서 1씩 더해지게 된다.
# 갈라지는 길에서 이미 방문한 상태라면 그때 가지고 있는 경우의 수를 리턴한다.