import math, heapq
from collections import defaultdict

class Deer:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def get_distance(self, y, x):
        return math.pow(self.y - y, 2) + math.pow(self.x - x, 2)
    
    def __str__(self):
        return f"루돌프: {self.y}, {self.x}"

class Santa:
    def __init__(self, y, x, id):
        self.y = y
        self.x = x
        self.id = id
        self.sleep = -1
        self.score = 0
        self.live = True

    def get_distance(self, y, x):
        return math.pow(self.y - y, 2) + math.pow(self.x - x, 2)

    def __str__(self):
        return f"산타 {self.id}: {self.y}, {self.x} / {'생존' if self.live else '탈락'} / 점수: {self.score} / 기절 턴: {self.sleep}"

def move_deer(turn):
    # 가장 가까운 산타 향해 1칸, 행렬 큰 기준
    dys = [-1, -1, -1, 0, 0, 1, 1, 1]
    dxs = [-1, 0, 1, -1, 1, -1, 0, 1]

    hq = []

    for santa in santas[1:]:
        if not santa.live:
            continue
        heapq.heappush(hq, (santa.get_distance(deer.y, deer.x), -santa.y, -santa.x, santa))

    target = heapq.heappop(hq)[-1]
    # print("타겟: ", target)
    min_distance = INF
    min_point = (-1, -1)
    min_direction = (INF, INF)

    for dy, dx in zip(dys, dxs):
        ny, nx = deer.y + dy, deer.x + dx

        if not in_range(ny, nx):
            continue
        
        distance = target.get_distance(ny, nx)
        if min_distance > distance:
            min_distance = distance
            min_point = (ny, nx)
            min_direction = (dy, dx)

    deer.y, deer.x = min_point
    pushed_santa = santas_point[min_point]
    santas_point[min_point] = None

    if pushed_santa:
        pushed_santa.score += C
        collision(pushed_santa, min_direction, C)
        pushed_santa.sleep = turn    
    

def move_santa(turn):
    # 거리 가까워지는 방향 1칸 이동
    # 다른 산타나 게임판 밖x, 없으면 가만히
    # 가까워지는 방법 없어도 가만히
    # 상우하좌

    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    for santa in santas[1:]:
        if not santa.live or santa.sleep + 1 >= turn:
            continue
        
        min_distance = deer.get_distance(santa.y, santa.x)
        min_point = (santa.y, santa.x)
        min_direction = (0, 0)

        for dy, dx in zip(dys, dxs):
            ny, nx = santa.y + dy, santa.x + dx

            if not in_range(ny, nx) or santas_point[(ny, nx)]:
                continue
            

            distance = deer.get_distance(ny, nx)

            if min_distance > distance:
                min_distance = distance
                min_point = (ny, nx)
                min_direction = (dy, dx)

        santas_point[(santa.y, santa.x)] = None
        santa.y, santa.x = min_point
        
        if min_point == (deer.y, deer.x):
            santa.score += D
            collision(santa, (-min_direction[0], -min_direction[1]), D)
            santa.sleep = turn
        else:
            santas_point[min_point] = santa


def collision(santa, direction, amount):
    # direction 방향으로 amount만큼 밀려나기
    # 기절시키기
    dy, dx = direction
    sy, sx = santa.y + (dy * amount), santa.x + (dx * amount)
    
    if not in_range(sy, sx):
        santa.live = False
        return

    if not santas_point[(sy, sx)]:
        santa.y, santa.x = sy, sx
        santas_point[(sy, sx)] = santa
        return

    pushed = []

    ny, nx = sy, sx
    
    while santas_point[(ny, nx)]:
        pushed.append(santas_point[(ny, nx)])
        ny, nx = ny + dy, nx + dx
    
    santa.y, santa.x = sy, sx
    santas_point[(sy, sx)] = santa

    ny, nx = sy + dy, sx + dx

    for pushed_santa in pushed:
        if in_range(ny, nx):
            pushed_santa.y, pushed_santa.x = ny, nx
            santas_point[(ny, nx)] = pushed_santa
        else:
            pushed_santa.live = False

        ny, nx = ny + dy, nx + dx

def in_range(y, x):
    return 1 <= y <= N and 1 <= x <= N

def get_score():
    for santa in santas[1:]:
        if santa.live:
            santa.score += 1

N, M, P, C, D = map(int, input().split())
RR, RC = map(int, input().split())
deer = Deer(RR, RC)

santas = [None for _ in range(P + 1)]
santas_point = defaultdict(lambda: None)

for _ in range(P):
    PN, SR, SC = map(int, input().split())
    santas[PN] = Santa(SR, SC, PN)
    santas_point[(SR, SC)] = santas[PN]

INF = int(1e9)

for turn in range(1, M+1):
    # print(turn, "턴")
    move_deer(turn)
    move_santa(turn)
    get_score()

    for santa in santas[1:]:
        if santa.live:
            break
    else:
        break

for santa in santas[1:]:
    print(santa.score, end=" ")