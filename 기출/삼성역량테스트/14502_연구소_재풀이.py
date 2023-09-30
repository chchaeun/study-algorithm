from collections import deque

N, M = map(int, input().split())
init = [list(map(int, input().split())) for _ in range(N)]

EMPTY, WALL, VIRUS = 0, 1, 2

def spread(board):
    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for v in virus:
        sy, sx = v
        visited[sy][sx] = True

        dq = deque([(sy, sx)])
        
        while dq:
            y, x = dq.popleft()
            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx

                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and board[ny][nx] != WALL:
                    board[ny][nx] = VIRUS
                    visited[ny][nx] = True
                    dq.append((ny, nx))
    
def safe(board):
    count = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == EMPTY:
                count += 1
    
    return count

global answer
answer = 0

empty, virus = [], []

for i in range(N):
    for j in range(M):
        if init[i][j] == EMPTY:
            empty.append((i, j))
        if init[i][j] == VIRUS:
            virus.append((i, j))
            
def wall(arr, depth):
    global answer
    if len(arr) == 3:
        board = [i[:] for i in init]
        for a in arr:
            y, x = a
            board[y][x] = WALL
        spread(board)
        answer = max(answer, safe(board))
        return
    if len(empty) == depth:
        return

    arr.append(empty[depth])
    wall(arr, depth + 1)

    arr.pop()
    wall(arr, depth + 1)

wall([], 0)
print(answer)