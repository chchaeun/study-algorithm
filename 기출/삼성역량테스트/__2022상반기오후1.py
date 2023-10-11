from collections import deque
EMPTY, HEAD, MEMBER, TAIL, LINE = 0, 1, 2, 3, 4
N, M, K = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(sy, sx, team):

    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
    dq = deque([(sy, sx)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sy][sx] = True
    move_line = [(sy, sx)]

    board[sy][sx] = team
    head, tail = 0, -1

    while dq:
        y, x = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if input_arr[ny][nx] == EMPTY:
                    continue
                if (y, x) == (sy, sx) and input_arr[ny][nx] == MEMBER or (sy, sx) != (y, x):
                    dq.append((ny, nx))
                    visited[ny][nx] = True
                    move_line.append((ny, nx))

                    if input_arr[ny][nx] != LINE:
                        board[ny][nx] = team

                    if input_arr[ny][nx] == TAIL:
                        tail = len(move_line)-1

    line.append(move_line)
    headtail.append([head, tail])
    direction.append(-1)

def move(team):
    h, t = headtail[team]

    ty, tx = line[team][t]
    nhy, nhx = line[team][(h+direction[team]) % len(line[team])]
    nty, ntx = line[team][(t-direction[team]) % len(line[team])]
    board[nhy][nhx], board[ty][tx] = team, board[nty][ntx]

    headtail[team] = [(h+direction[team])%len(line[team]), (t+direction[team])%len(line[team])]

def get_score(y, x):
    global answer

    score = 0
    team = board[y][x]
    h, t = headtail[team]

    idx = line[team].index((y, x))
    if direction[team] == -1:
        if h < idx:
            score = idx - h + 1
        elif h > idx:
            score = len(line[team])-(h-idx) + 1
        else:
            score = 1
    else:
        if h < idx:
            score = len(line[team])-(idx-h) + 1
        elif h > idx:
            score = h-idx + 1
        else:
            score = 1

    headtail[team] = [t, h]
    direction[team] *= -1

    answer += score * score

global answer
answer = 0
headtail = []
direction = []
line = []
board = [[-1 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if input_arr[i][j] == HEAD:
            bfs(i, j, len(headtail))


for i in range(len(headtail)):
    move(i)

def rounds(i, j, turn):
    if turn == 0:
        return (i, j)
    elif turn == 1:
        return (N-1-j, i)
    elif turn==2:
        return (N - 1 - i, N - 1 - j)
    else:
        return (j, N - 1 - i)

round = 1
while round <= K:
    for turn in range(4):
        for i in range(N):
            for j in range(N):
                a, b = rounds(i, j, turn)
                if board[a][b] > -1:
                    get_score(a, b)
                    break

            round += 1

            if round > K:
                print(answer)
                exit()

            for k in range(len(headtail)):
                move(k)