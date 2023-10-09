from collections import defaultdict, deque
CHECK = 5
R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
checks = []
heat = defaultdict(int)
wall = defaultdict(bool)
temp = defaultdict(int)
direction = [(0, 1),(0, -1),(-1, 0),(1, 0)]

for i in range(R):
    for j in range(C):
        if board[i][j] == CHECK:
            checks.append((i, j))
        elif board[i][j] > 0:
            heat[(i, j)] = board[i][j] - 1

W = int(input())
for _ in range(W):
    y, x, t = map(int, input().split())
    y, x = y-1, x-1
    if t == 0:
        wall[((y-1, x), (y, x))] = True
    else:
        wall[((y, x), (y, x+1))] = True

def is_wall(a, b):
    return wall[tuple(sorted([a, b]))]

def mount():
    mount = defaultdict(int)
    for point, d in heat.items():
        sy, sx = point
        dy, dx = direction[d]
        sy, sx = sy + dy, sx + dx

        mount[(sy, sx)] += 5

        dq = deque([(sy, sx, 5)])
        visited = defaultdict(bool)
        visited[(sy, sx)] = True

        while dq:
            y, x, t = dq.popleft()
            can_spread = []
            # 정면
            if not is_wall((y, x), (y + dy, x + dx)):
                can_spread.append((y + dy, x + dx))
            # 대각선
            if not is_wall((y, x), (y - dx, x - dy)) and not is_wall((y - dx, x - dy), (y - dx + dy, x - dy + dx)):
                can_spread.append((y - dx + dy, x - dy + dx))
            if not is_wall((y, x), (y + dx, x + dy)) and not is_wall((y + dx, x + dy), (y + dx + dy, x + dy + dx)):
                can_spread.append((y + dx + dy, x + dy + dx))

            for cs in can_spread:
                ny, nx = cs
                if 0 <= ny < R and 0 <= nx < C and t != 1 and not visited[(ny, nx)]:
                    mount[(ny, nx)] += t-1
                    dq.append((ny, nx, t-1))
                    visited[(ny, nx)] = True
    return mount

def wind():
    for key, value in wind_mount.items():
        temp[key] += value

def change():
    change_temp = defaultdict(int)
    keys = list(temp.keys()).copy()

    for key in keys:
        y, x = key
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and temp[(y, x)] > temp[(ny, nx)] and not is_wall((y, x), (ny, nx)):
                d = (temp[(y, x)] - temp[(ny, nx)]) // 4
                change_temp[(y, x)] -= d
                change_temp[(ny, nx)] += d

    for key in change_temp.keys():
        y, x = key
        temp[(y, x)] += change_temp[(y, x)]

def down(i, j):
    if temp[(i, j)] > 0:
        temp[(i, j)] -= 1

def outline():
    for i in range(C):
        down(0, i)
        down(R-1, i)
    for i in range(1, R-1):
        down(i, 0)
        down(i, C-1)

def check():
    for c in checks:
        y, x = c
        if temp[(y, x)] < K:
            return False
    return True

answer = 0
wind_mount = mount()

while answer < 101:
    wind()
    change()
    outline()
    answer += 1

    if check():
        break
print(answer)


