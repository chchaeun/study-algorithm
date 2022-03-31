import sys; input=sys.stdin.readline
n, m = map(int, input().split())
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
board = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    r, c = map(int, input().split())
    board[r][c] = 1
    count = 0
    for dx, dy in zip(dxs, dys):
        nr, nc = r+dx, c+dy
        if 0<=nr<n+1 and 0<=nc<n+1 and board[nr][nc] == 1:
            count += 1
    print(1 if count==3 else 0)