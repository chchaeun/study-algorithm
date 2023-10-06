EMPTY, WALL, HOLE, RED, BLUE = '.', '#', 'O', 'R', 'B'
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
location = {
    RED: [],
    BLUE: []
}

for i in range(N):
    for j in range(M):
        if board[i][j] == RED:
            location[RED] = [i, j]
        if board[i][j] == BLUE:
            location[BLUE] = [i, j]

def move(board, location_color, d):
    y, x = location_color
    dy, dx = d

    i = 1
    while True:
        ny, nx = y + dy * i, x + dx * i
        
        if board[ny][nx] != EMPTY:
            break
        
        i += 1
        
    if board[ny][nx] == HOLE:
        board[y][x] = EMPTY
        return (board, [])

    ny, nx = y + dy * (i-1), x + dx * (i-1)
    
    board[ny][nx], board[y][x] = board[y][x], board[ny][nx]

    return (board, [ny, nx])


def priority(location, d):
    ry, rx = location[RED]
    by, bx = location[BLUE]

    if d == 0 and ry > by:
        return (RED, BLUE)
    
    if d == 1 and ry < by:
        return (RED, BLUE)

    if d == 2 and rx > bx:
        return (RED, BLUE)

    if d == 3 and rx < bx:
        return (RED, BLUE)
    
    return (BLUE, RED)

global answer
answer = int(1e9)

def backtracking(board, location, history):
    global answer
    if len(history) == 10:
        return

    for i, d in enumerate(direction):
        nboard = [b[:] for b in board]
        nlocation = {
            RED: location[RED][:],
            BLUE: location[BLUE][:]
        }

        if history and history[-1] == i:
            continue
    
        p = priority(nlocation, i)
        drop = {
            RED: False,
            BLUE: False
        }

        for color in p:
            nboard, nlocation[color] = move(nboard, nlocation[color], d)
            drop[color] = len(nlocation[color]) == 0
        
        if drop[RED] and not drop[BLUE]:
            answer = min(answer, len(history)+1)
            continue

        if drop[RED] or drop[BLUE]:
            continue
        
        history.append(i)
        backtracking(nboard, nlocation, history)
        history.pop()

backtracking(board, location, [])
answer = -1 if answer == int(1e9) else answer
print(answer)