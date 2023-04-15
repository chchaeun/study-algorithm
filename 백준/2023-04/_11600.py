import sys
input = sys.stdin.readline
n, m = map(int, input().split())

board = [[0]*(n+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]
point = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    for j in range(n):
        board[i+1][j+1] = board[i][j+1] + board[i+1][j] + board[i+1][j+1] - board[i][j]  

for p in point:
    x1, y1, x2, y2 = p
    print(board[x2][y2] - board[x1-1][y2] - board[x2][y1-1] + board[x1-1][y1-1])