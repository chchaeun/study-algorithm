n, m, t = map(int, input().split())
board = [[None for _ in range(n)] for _ in range(n)]

direct = {
    'U':0,
    'R':1,
    'L':2,
    'D':3,
}

for i in range(m):
    r, c, d, w = input().split()
    board[int(r)-1][int(c)-1] = (i, direct[d], int(w))
    
dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]

for _ in range(t):
    nboard = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                num, d, w = board[i][j]
                nx, ny = i+dx[d], j+dy[d]
                if not (0<=nx<n and 0<=ny<n):
                    d = 3-d
                    nx, ny = i, j
                nboard[nx][ny].append((num, d, w))
    for i in range(n):
        for j in range(n):
            nboard[i][j].sort(reverse=True)
            if not nboard[i][j]:
                board[i][j] = None
            else:
                _sum = 0
                for nb in range(len(nboard[i][j])):
                    _sum += nboard[i][j][nb][2]
                board[i][j] = nboard[i][j][0][0], nboard[i][j][0][1], _sum
count = 0
_max = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            count += 1
            _max = max(_max, board[i][j][2])
print(count, _max)