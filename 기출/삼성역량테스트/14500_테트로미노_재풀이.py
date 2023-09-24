N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

global answer
answer = 0

visited = [[False for _ in range(M)] for _ in range(N)]
dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(y, x, depth, _sum):
    global answer
    if depth == 3:
        answer = max(answer, _sum)
        return

    for dy, dx in zip(dys, dxs):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, depth+1, _sum+board[ny][nx])
            visited[ny][nx] = False

def t_shape(i, j):
    global answer

    if j+2 < M:
        width_sum = sum(board[i][j:j+3])
        if 0 <= i-1:
            answer = max(answer, width_sum + board[i-1][j+1])
        if i+1 < N:
            answer = max(answer, width_sum + board[i+1][j+1])
    if i+2 < N:
        height_sum = board[i][j] + board[i+1][j] + board[i+2][j]
        if 0 <= j-1:
            answer = max(answer, height_sum + board[i+1][j-1])
        if j+1 < M:
            answer = max(answer, height_sum + board[i+1][j+1])
    

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, board[i][j])
        visited[i][j] = False
        t_shape(i, j)

print(answer)