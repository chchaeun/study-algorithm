import heapq
from collections import defaultdict, deque

BROKEN = 0
INF = int(1e9)

N, M, K = map(int, input().split())
power = [list(map(int, input().split())) for _ in range(N)]

last_attack = [[0 for _ in range(M)] for _ in range(N)]
dist = [[INF for _ in range(M)] for _ in range(N)]
attacked = defaultdict(bool)

def weak_strong(turn):
    hq = []

    for i in range(N):
        for j in range(M):
            if power[i][j] <= BROKEN:
                continue
            heapq.heappush(hq, (power[i][j], -last_attack[i][j], -(i+j), -j, (i, j)))

    weak = heapq.heappop(hq)[4]
    strong = heapq.nlargest(1, hq)[0][4]

    wy, wx = weak
    last_attack[wy][wx] = turn

    return weak, strong

def add_power(weak):
    y, x = weak
    power[y][x] += N+M

dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]
def short(strong):
    sy, sx = strong

    dist[sy][sx] = 0
    dq = deque([(sy, sx)])

    while dq:
        y, x = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = (y + dy) % N, (x + dx) % M

            if power[ny][nx] > BROKEN and dist[y][x] + 1 < dist[ny][nx]:
                dist[ny][nx] = dist[y][x] + 1
                dq.append((ny, nx))

def laser(weak, strong):
    _min, min_point = INF, (-1, -1)
    y, x = weak
    attack_power = power[y][x]
    while (y, x) != strong:
        for dy, dx in zip(dys, dxs):
            ny, nx = (y + dy) % N, (x + dx) % M

            if _min > dist[ny][nx]:
                _min = dist[ny][nx]
                min_point = (ny, nx)

        y, x = min_point

        if (y, x) == strong:
            power[y][x] -= attack_power
        else:
            power[y][x] -= attack_power // 2
        attacked[(y, x)] = True

def bomb(weak, strong):
    wy, wx = weak
    sy, sx = strong
    attack_power = power[wy][wx]
    power[sy][sx] -= attack_power
    attacked[(sy, sx)] = True

    direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dy, dx in direction:
        ny, nx = (sy + dy) % N, (sx + dx) % M
        if power[ny][nx] > BROKEN and (ny, nx) != weak:
            power[ny][nx] -= attack_power // 2
            attacked[(ny, nx)] = True

def fix(weak):
    count = 0
    for i in range(N):
        for j in range(M):
            if power[i][j] > BROKEN:
                count += 1
                if not attacked[(i, j)] and (i, j) != weak:
                    power[i][j] += 1

    if count == 1:
        return False
    return True

for turn in range(1, K+1):
    weak, strong = weak_strong(turn)
    add_power(weak)
    short(strong)
    wy, wx = weak
    if dist[wy][wx] == INF:
        bomb(weak, strong)
    else:
        laser(weak, strong)
    if not fix(weak):
        break
    dist = [[INF for _ in range(M)] for _ in range(N)]
    attacked = defaultdict(bool)

print(max(list(max(p) for p in power)))