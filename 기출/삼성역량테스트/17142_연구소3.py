from collections import deque

INF = int(1e9)
EMPTY, WALL, VIRUS = 0, 1, 2
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def visit(sy, sx):
    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
    visited = [[INF for _ in range(N)] for _ in range(N)]

    dq = deque([(sy, sx)])
    visited[sy][sx] = 0

    while dq:
        y, x = dq.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] != WALL and visited[ny][nx] > visited[y][x] + 1:
                    dq.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1

    return [v[:] for v in visited]

def nCr(arr, M, depth):
    if len(arr) == M:
        merge(arr)
        return
    if len(virus_visited) == depth:
        return

    arr.append(virus_visited[depth])
    nCr(arr, M, depth + 1)

    arr.pop()
    nCr(arr, M, depth + 1)

answer = INF


def merge(combinated):
    mvisited = [[INF for _ in range(N)] for _ in range(N)]
    for c in combinated:
        for i in range(N):
            for j in range(N):
                    mvisited[i][j] = min(c[i][j], mvisited[i][j])
    minimum(mvisited)

def minimum(mvisited):
    global answer
    result = 0
    for i in range(N):
        for j in range(N):
            if mvisited[i][j] == INF and board[i][j] == EMPTY:
                result = INF
                break
    
            if mvisited[i][j] != INF and board[i][j] != VIRUS:
                result = max(mvisited[i][j], result)

    answer = min(answer, result)

virus_visited = []
for i in range(N):
    for j in range(N):
        if board[i][j] == VIRUS:
            virus_visited.append(visit(i, j))


nCr([], M, 0)
answer = -1 if answer == INF else answer
print(answer)

