N = 4
EMPTY, SHARK = 0, -1
first_board = [[None for _ in range(N)] for _ in range(N)]

for i in range(N):
    input_arr = list(map(int, input().split()))
    for j in range(0, N * 2, 2):
        first_board[i][j//2] = [input_arr[j], input_arr[j+1]-1]

direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def one_fish_move(num, board):
    for y in range(N):
        for x in range(N):
            if board[y][x][0] == num:
                for _ in range(8):
                    dy, dx = direction[board[y][x][1]]
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N and board[ny][nx][0] != SHARK:
                        board[ny][nx], board[y][x] = board[y][x], board[ny][nx]
                        return
                    board[y][x][1] = (board[y][x][1] + 1) % 8

def fish_move(board):
    for num in range(1, N*N+1):
        one_fish_move(num, board)
    return board
def shark_move(board, eat):
    board = [[el[:] for el in b] for b in board]
    board = fish_move(board)

    global answer
    for i in range(N):
        for j in range(N):
            if board[i][j][0] == SHARK:
                y, x, d = i, j, board[i][j][1]

    dy, dx = direction[d]
    for k in range(1, 4):
        ny, nx = y + dy * k, x + dx * k

        if not (0 <= ny < N and 0 <= nx < N) or board[ny][nx][0] == EMPTY:
            answer = max(answer, eat)
            continue
        old_fish = board[ny][nx][0]
        board[ny][nx][0] = SHARK
        board[y][x][0] = EMPTY

        shark_move(board, eat + old_fish)

        board[y][x][0] = SHARK
        board[ny][nx][0] = old_fish

global answer
answer = first_board[0][0][0]

first_board[0][0][0] = -1

shark_move(first_board, answer)
print(answer)