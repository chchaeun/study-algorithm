n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

x, y = n-1, n-1
cur = 0
for i in range(n*n, 0, -1):
    board[x][y] = i
    nx, ny = x + dx[cur], y + dy[cur]
    if not (0<=nx<n and 0<=ny<n) or board[nx][ny]:
        cur = (cur+1)%4
    x, y = x + dx[cur], y + dy[cur]

for b in board:
    print(*b)