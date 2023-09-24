from collections import deque

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dice = [[2, 1, 5, 6], [4, 1, 3, 6]]

global pos, direction
pos = [0, 0]
direction = 0

def roll():
    global direction
    up, down = dice

    if direction == 0:
        down = [down[-1]] + down[:-1]
        up[1], up[3] = down[1], down[3]
    if direction == 1:
        up = [up[-1]] + up[:-1]
        down[1], down[3] = up[1], up[3]
    if direction == 2:
        down = down[1:] + [down[0]]
        up[1], up[3] = down[1], down[3]
    if direction == 3:
        up = up[1:] + [up[0]]
        down[1], down[3] = up[1], up[3]
    
    dice[0], dice[1] = up, down

dys, dxs = (0, 1, 0, -1), (1, 0, -1, 0)

def move():
    global pos, direction
    y, x = pos
    ny, nx = y + dys[direction], x + dxs[direction]
    if 0 <= ny < N and 0 <= nx < M:
        pos = [ny, nx]
        return
    direction = (direction + 2) % 4
    pos = [y + dys[direction], x + dxs[direction]]


def score():
    sy, sx = pos
    now = board[sy][sx]
    count = 1

    dq = deque([(sy, sx)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[sy][sx] = True

    while dq:
        y, x = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and board[ny][nx] == now:
                dq.append((ny, nx))
                visited[ny][nx] = True
                count += 1
    return now * count

def next_direction():
    global direction
    a = dice[1][3]
    y, x = pos
    b = board[y][x]

    if a > b:
        direction = (direction + 1) % 4
    if a < b:
        direction = (direction - 1) % 4

answer = 0

for _ in range(K):
    move()
    roll()
    answer += score()
    next_direction()

print(answer)