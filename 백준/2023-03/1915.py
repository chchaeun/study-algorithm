def in_range(y, x):
    return 0 <= y < N and 0 <= x < M

EMPTY, FILL = '0', '1'
N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]

for b in board:
    print(*b)

for i in range(1, N):
    for j in range(1, M):
        if board[i][j] == 0:
            continue
        board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1

print(max(list(max(b) for b in board)) ** 2)
