EMPTY = 0
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def ice(d, s):
    y, x = (N+1)//2-1, (N+1)//2-1
    dy, dx = direction[d]
    for i in range(1, s+1):
        board[y + dy * i][x + dx * i] = EMPTY

def tornado(do):
    anticlockwise = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    y, x, d = (N+1)//2-1, (N+1)//2-1, 0
    unit = 1
    
    while y > -1 and x > -1:
        for _ in range(2):
            dy, dx = anticlockwise[d % 4]
            for _ in range(unit):
                y, x = y + dy, x + dx
                do(y, x)
                if y == 0 and x == 0:
                    return
            d += 1
        unit += 1

global answer
answer = 0

def bang(arr):
    global answer
    breaking = False

    while not breaking:
        narr = []
        breaking = True
        count = 0
        for a in arr:
            if not narr or narr[-1] == a:
                narr.append(a)
                count += 1
            else:
                if count >= 4:
                    for _ in range(count):
                        answer += narr.pop()
                    breaking = False

                narr.append(a)
                count = 1
        
        if count >= 4:
            for _ in range(count):
                answer += narr.pop()

        arr = narr.copy()

    return group(arr)

def group(arr):
    narr = []
    for a in arr:
        if not narr or narr and narr[-1] != a:
            narr.extend([1, a])
        else:
            narr[-2] += 1
    return narr

def make_arr(y, x):
    if board[y][x] == EMPTY:
        return

    arr.append(board[y][x])

def make_board(y, x):
    global i
    if i < len(arr):
        nboard[y][x] = arr[i]
    i += 1

for _ in range(M):
    global i
    i = 0
    arr, nboard = [], [[EMPTY for _ in range(N)] for _ in range(N)]
    d, s = map(int, input().split())

    ice(d-1, s)
    tornado(make_arr)
    arr = bang(arr)
    tornado(make_board)

    board = [nb[:] for nb in nboard]

print(answer)