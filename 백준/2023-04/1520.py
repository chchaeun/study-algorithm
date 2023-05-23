import sys
sys.setrecursionlimit(10 ** 9)

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1 for _ in range(N)] for _ in range(M)]

def in_range(y, x):
    return 0 <= y < M and 0 <= x < N

def dfs(y, x):
    if y == M - 1 and x == N - 1:
        return 1

    if dp[y][x] == -1:
        dp[y][x] = 0
        
        dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx

            if in_range(ny, nx) and board[ny][nx] < board[y][x]:
                dp[y][x] += dfs(ny, nx)

    return dp[y][x]
    
print(dfs(0, 0))