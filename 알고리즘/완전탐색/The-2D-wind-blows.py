from copy import deepcopy
import sys; input=sys.stdin.readline
n, m, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def rotate(r1, c1, r2, c2):
    temp = board[r1][c1]
    for i in range(r1, r2):
        board[i][c1] = board[i+1][c1]
    for i in range(c1, c2):
        board[r2][i] = board[r2][i+1]
    for i in range(r2, r1, -1):
        board[i][c2] = board[i-1][c2]
    for i in range(c2, c1, -1):
        board[r1][i] = board[r1][i-1]
    board[r1][c1+1] = temp

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
def average(r1, c1, r2, c2):
    nboard = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            count = 1
            _sum = board[i][j]
            for dx, dy in zip(dxs, dys):
                nx, ny = i+dx, j+dy
                if 0<=nx<n and 0<=ny<m:
                    count += 1
                    _sum += board[nx][ny]
            nboard[i][j] = _sum//count
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            board[i][j] = nboard[i][j]
        
for _ in range(q):
    r1, c1, r2, c2 = map(lambda x: int(x)-1, input().split())
    rotate(r1, c1, r2, c2)
    average(r1, c1, r2, c2)
    
for b in board:
    print(*b)
    
    