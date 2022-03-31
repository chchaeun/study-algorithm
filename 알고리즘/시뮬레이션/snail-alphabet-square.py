n, m = map(int, input().split())
board = [['' for _ in range(m)] for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0
cur = 0
for i in range(n*m):
    alpha = (i%26)+65
    board[x][y] = chr(alpha)
    nx, ny = x+dx[cur], y+dy[cur]
    if not (0<=nx<n and 0<=ny<m) or board[nx][ny]:
        cur = (cur+1)%4
    x, y = x+dx[cur], y+dy[cur]
    
for b in board:
    print(*b)