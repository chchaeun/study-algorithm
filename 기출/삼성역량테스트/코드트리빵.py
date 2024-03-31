import heapq
from collections import deque

class Player:
    def __init__(self, id):
        self.id = id
        self.y = -1
        self.x = -1
        self.success = False
    
    def __str__(self):
        return f"{self.id}: {self.y}, {self.x} / 성공: {self.success}"

class Shop:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    
    def get_distance(self):
        dys = [-1, 0, 0, 1]
        dxs = [0, -1, 1, 0]

        distance = [[int(1e9) for _ in range(N)] for _ in range(N)]
        distance[self.y][self.x] = 0
        dq = deque([(self.y, self.x)])

        while dq:
            y, x = dq.popleft()

            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx

                if in_range(ny, nx) and can_visit[ny][nx] and distance[ny][nx] > distance[y][x] + 1:
                    distance[ny][nx] = distance[y][x] + 1
                    dq.append((ny, nx))

        return distance

class Base:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.choosed = False

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def move(id):
    dys = [-1, 0, 0, 1]
    dxs = [0, -1, 1, 0]

    player = players[id]
    shop = shops[id]

    distance = shop.get_distance()


    hq = []

    for dy, dx in zip(dys, dxs):
        ny, nx = player.y + dy, player.x + dx

        if in_range(ny, nx) and can_visit[ny][nx]:
            heapq.heappush(hq, (distance[ny][nx], (ny, nx)))

    my, mx = heapq.heappop(hq)[-1]
    player.y, player.x = my, mx

    if (player.y, player.x) == (shop.y, shop.x):
        player.success = True

def choose_base(id):
    player = players[id]
    shop = shops[id]
    distance = shop.get_distance()

    hq = []

    for base in bases:
        if not base.choosed:
            heapq.heappush(hq, (distance[base.y][base.x], (base.y, base.x), base))

    mbase = heapq.heappop(hq)[-1]
    player.y, player.x = mbase.y, mbase.x
    mbase.choosed = True    

N, M = map(int, input().split())
players = [Player(id) for id in range(M + 1)]
shops = [None for _ in range(M + 1)]
bases = []
can_visit = [[True for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j, base in enumerate(list(map(int, input().split()))):
        if base == 1:
            bases.append(Base(i, j))

for id in range(1, M + 1):
    y, x = map(int, input().split())
    shops[id] = Shop(y - 1, x - 1)


time = 1

while True:
    for id in range(1, M + 1):
        if time > id and not players[id].success:
            move(id)

    success_count = 0

    for player in players[1:]:
        if player.success:
            can_visit[player.y][player.x] = False
            success_count += 1

    if time <= M:
        choose_base(time)

    if success_count == M:
        break

    for base in bases:
        if base.choosed:
            can_visit[base.y][base.x] = False

    time += 1

print(time)

print()
for player in players[1:]:
    print(player)
print()

for i in range(N):
    for j in range(N):
        print(can_visit[i][j], end=" ")
    print()
print()