N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 if i == j else int(1e9) for j in range(N)] for i in range(N)]

for i in range(1, N):
    y, x = 0, i

    while 0 <= y < N and 0 <= x < N:

        for j in range(x):
            if (y + j + 1 > x):
                break

            dp[y][x] = min(dp[y][x], dp[y][y+j] + dp[y+j+1][x] + board[y][0] * board[y+j][1] * board[x][1])

        y += 1
        x += 1

print(dp[0][N-1])