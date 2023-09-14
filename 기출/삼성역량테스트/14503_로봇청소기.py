n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

UNCLEAN, WALL, CLEAN = 0, 1, 2
answer = 0

clockwise = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 시계방향

while True:
    if board[r][c] == UNCLEAN:
        board[r][c] = CLEAN
        answer += 1
    for i in range(1, 5):
        nd = (d-i+4) % 4
        dy, dx = clockwise[nd]
        if board[r+dy][c+dx] == UNCLEAN:
            r, c, d = r+dy, c+dx, nd
            break
    else:
        dy, dx = clockwise[d]
        ny, nx = r-dy, c-dx
        if board[ny][nx] == WALL:
            break
        r, c = ny, nx
print(answer)
