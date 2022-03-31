n, m = map(int, input().split())
board = [[0]*m for _ in range(n)]
x, y = 0, -1
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cur = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<m

for i in range(1, n*m+1):
    nx, ny = x+dx[cur], y+dy[cur]
    if not in_range(nx, ny) or board[nx][ny]!=0:
        cur = (cur+1)%4
        nx, ny = x+dx[cur], y+dy[cur]
    board[nx][ny] = i
    x, y = nx, ny
    
    for b in board:
        print(*b)
    print()
