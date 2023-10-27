from collections import deque

N, M, K = map(int, input().split())
EMPTY, EXIT = 0, 11
INF = int(1e9)

board = [list(map(lambda x: -int(x), input().split())) for _ in range(N)]
for _ in range(M):
    y, x = map(int, input().split())
    board[y-1][x-1] += 1
ey, ex = map(int, input().split())
ey, ex = ey - 1, ex - 1
board[ey][ex] = EXIT
dys, dxs = [1, -1, 0, 0], [0, 0, -1, 1]

global moving
moving = 0
def move(ey, ex):
    global moving
    nboard = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] <= EMPTY or board[i][j] == EXIT:
                continue
            _min, min_point = abs(ey-i) + abs(ex-j), (i, j)
            for dy, dx in zip(dys, dxs):
                ny, nx = i + dy, j + dx
                dist = abs(ey-ny) + abs(ex-nx)
                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] >= EMPTY and _min > dist:
                    _min = dist
                    min_point = (ny, nx)
            y, x = min_point
            if (i, j) != (y, x):
                moving += board[i][j]

            if board[y][x] != EXIT:
                nboard[y][x] += board[i][j]
            board[i][j] = 0

    for i in range(N):
        for j in range(N):
            board[i][j] += nboard[i][j]

def check(y, x, size):
    exit = False
    person = False
    for i in range(size):
        for j in range(size):
            if not (0 <= y + i < N and 0 <= x+j < N):
                return False
            if board[y+i][x+j] == EXIT:
                exit = True
            if EMPTY < board[y+i][x+j] < EXIT:
                person = True

    return exit and person
def square():
    for size in range(2, N+1):
        for i in range(N):
            for j in range(N):
                if check(i, j, size):
                    return i, j, size

def rotate(ey, ex):
    y, x, size = square()
    nboard = [[None for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            nboard[i][j] = board[y+size-1-j][x+i]

    for i in range(size):
        for j in range(size):
            if nboard[i][j] < EMPTY:
                board[y+i][x+j] = nboard[i][j] + 1
            else:
                board[y+i][x+j] = nboard[i][j]

for turn in range(K):
    move(ey, ex)
    count = 0
    for i in range(N):
        for j in range(N):
            if EMPTY < board[i][j] < EXIT:
                count += 1
    if count == 0:
        break

    rotate(ey, ex)

    for i in range(N):
        for j in range(N):
            if board[i][j] == EXIT:
                ey, ex = i, j

print(moving)
print(ey+1, ex+1)