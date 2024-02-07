N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
values = [[0 if i==j else int(1e9) for j in range(N)] for i in range(N)]

for i in range(1, N):
    y, x = 0, i

    while 0 <= y < N and 0 <= x < N:

        for i in range(x):
            if (y + i + 1 > x):
                break
            print(y, y + i, y + i + 1, x)

            values[y][x] = min(values[y][x], values[y][y+i] + values[y+i+1][x] + board[y][0] * board[y+i][1] * board[x][1])

        y += 1
        x += 1

print(values[0][N-1])