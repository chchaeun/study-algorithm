from collections import defaultdict, deque

EMPTY = ' '
N = int(input())

def bfs(sy, sx, name):
    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
    dq = deque([(sy, sx)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sy][sx] = True
    group[sy][sx] = name
    count_group[name] = 1
    num_group[name] = board[sy][sx]
    while dq:
        y, x = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N:
                if board[y][x] != board[ny][nx] and group[ny][nx] == EMPTY:
                    around_group[name].append((ny, nx))
                elif not visited[ny][nx] and board[y][x] == board[ny][nx]:
                    group[ny][nx] = name
                    count_group[name] += 1
                    dq.append((ny, nx))
                visited[ny][nx] = True

def rotate():
    nboard = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        nboard[N//2][i] = board[i][N//2]
        nboard[i][N//2] = board[N//2][N-i-1]

    starts = [(0, 0), (0, N//2+1), (N//2+1, 0), (N//2+1, N//2+1)]
    for start in starts:
        y, x = start
        for i in range(N//2):
            for j in range(N//2):
                nboard[y+i][x+j] = board[y + N//2-1-j][x + i]

    return nboard
    
answer = 0
board = [list(map(int, input().split())) for _ in range(N)]

for t in range(4):
    group = [[EMPTY for _ in range(N)] for _ in range(N)]
    count_group = defaultdict(int)
    around_group = defaultdict(list)
    num_group = defaultdict(int)

    name = 65
    for i in range(N):
        for j in range(N):
            if group[i][j] == EMPTY:
                bfs(i, j, chr(name))
                name += 1

    groups = list(count_group.keys())
    total = 0
    for i in range(len(groups)-1):
        for j in range(i+1, len(groups)):
            g1, g2 = groups[i], groups[j]

            near = 0
            for ag in around_group[g1]:
                y, x = ag
                if group[y][x] == g2:
                    near += 1

            total += (count_group[g1] + count_group[g2]) * num_group[g1] * num_group[g2] * near
    answer += total

    if t == 3:
        break

    board = rotate()

print(answer)

