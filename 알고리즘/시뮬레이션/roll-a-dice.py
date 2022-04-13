n, m, r, c = map(int, input().split())
r, c = r-1, c-1
order = list(input().split())

board = [[0]*n for _ in range(n)]
board[r][c] = 6

direct = {
    'L':0,
    'R':1,
    'U':2,
    'D':3
}
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

top, left, right = 1, 2, 3

for i in range(m):
    dir = direct[order[i]]
    nx, ny = r+dx[dir], c+dy[dir]
    if 0<=nx<n and 0<=ny<n:
        r, c = nx, ny
        if dir==0:
            top, right = right, 7-top
        elif dir==1:
            top, right = 7-right, top
        elif dir==2:
            top, left = left, 7-top
        else:
            top, left = 7-left, top
        board[r][c] = 7-top

print(sum(list(map(sum, board))))