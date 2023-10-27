from collections import defaultdict, deque

N, M = map(int, input().split())
basecamp = [list(map(int, input().split())) for _ in range(N)]

cant_go = defaultdict(bool)

store = [None for _ in range(M)]
location = [None for _ in range(M)]
way = [[[int(1e9) for _ in range(N)] for _ in range(N)] for _ in range(M)]

for i in range(M):
    y, x = map(int, input().split())
    store[i] = (y-1, x-1)

dys, dxs = [-1, 0, 0, 1], [0, -1, 1, 0]
def move(num):
    if location[num] is None or location[num] == store[num]:
        return

    y, x = location[num]
    move_min, move_point = int(1e9), (y, x)

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < N and not cant_go[(ny, nx)] and move_min > way[num][ny][nx]:
            move_min = way[num][ny][nx]
            move_point = (ny, nx)

    location[num] = move_point

    if location[num] == store[num]:
        cant_go[move_point] = True

def short(num):
    if location[num] == store[num]:
        return

    sy, sx = store[num]
    dq = deque([(sy, sx)])
    way[num][sy][sx] = 0

    while dq:
        y, x = dq.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and way[num][ny][nx] > way[num][y][x] + 1 and not cant_go[(ny, nx)]:
                way[num][ny][nx] = way[num][y][x] + 1
                dq.append((ny, nx))

def base(num):
    _min, min_point = int(1e9), (-1, -1)
    sy, sx = store[num]
    for i in range(N):
        for j in range(N):
            if _min > way[num][i][j] and basecamp[i][j] == 1 and not cant_go[(i, j)]:
                _min = way[num][i][j]
                min_point = (i, j)

    location[num] = min_point
    cant_go[min_point] = True

t = 1
while True:
    way = [[[int(1e9) for _ in range(N)] for _ in range(N)] for _ in range(M)]
    for i in range(min(t, M)):
        short(i)
        move(i)

    breaking = True
    for s, l in zip(store, location):
        if s != l:
            breaking = False

    if breaking:
        print(t)
        break

    if t <= M:
        way = [[[int(1e9) for _ in range(N)] for _ in range(N)] for _ in range(M)]
        short(t-1)
        base(t-1)

    t += 1
