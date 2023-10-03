N = int(input())
EMPTY, BLOCK = 0, 1
W, H = 4, 6
shape = {1: [(0, 0)], 2: [(0, 0), (0, 1)], 3: [(0, 0), (1, 0)]}
green = [[EMPTY for _ in range(W)] for _ in range(H)]
blue = [[EMPTY for _ in range(W)] for _ in range(H)]

def put(t, x, board):
    y = 0

    while True:
        flag = False
        for s in shape[t]:
            dy, dx = s
            ny, nx = y+dy, x+dx
            if not (0 <= ny < H and 0 <= nx < W) or board[ny][nx] == BLOCK:
                flag = True
                break
        if flag:
            y -= 1
            for s in shape[t]:
                dy, dx = s
                ny, nx = y+dy, x+dx
                board[ny][nx] = BLOCK
            break

        y += 1

    return board

def erase(board):
    global score
    
    nboard = []
    for b in board:
        if EMPTY in b:
            nboard.append(b)
            continue
        score += 1

    nboard = [[EMPTY]*W for _ in range(H-len(nboard))] + nboard

    return special(nboard)

def special(board):
    count = 0
    for b in board[:2]:
        if BLOCK in b:
            count += 1

    if count == 0:
        return board

    return [[EMPTY] * W for _ in range(count)] + board[:H-count]

global score
score = 0

for _ in range(N):
    t, y, x = map(int, input().split())
    green = put(t, x, green)
    green = erase(green)

    if t == 1:
        y, x = x, 3-y
    elif t == 2:
        t, y, x = 3, x, 3-y
    elif t == 3:
        t, y, x = 2, x, 2-y
    
    blue = put(t, x, blue)
    blue = erase(blue)

total = 0

for i in range(H):
    for j in range(W):
        if green[i][j] == BLOCK:
            total += 1
        if blue[i][j] == BLOCK:
            total += 1

print(score)
print(total)