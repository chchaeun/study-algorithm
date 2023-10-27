from collections import defaultdict
EMPTY = 0
clockwise = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M, K = map(int, input().split())
guns = [list(map(lambda i: [int(i)] if int(i) > 0 else [], input().split())) for _ in range(N)]
players = [[EMPTY for _ in range(N)] for _ in range(N)]

location = [None for _ in range(M+1)]
direction = [None for _ in range(M+1)]
power_gun = [None for _ in range(M+1)]
point = [0 for _ in range(M+1)]

for num in range(1, M+1):
    y, x, d, s = map(int, input().split())
    location[num] = (y-1, x-1)
    direction[num] = d
    power_gun[num] = [s, 0]
    players[y-1][x-1] = num

def move():
    for num in range(1, M+1):
        y, x = location[num]
        dy, dx = clockwise[direction[num]]

        ny, nx = y + dy, x + dx

        if not (0<=ny<N and 0<=nx<N):
            direction[num] = (direction[num] + 2) % 4
            dy, dx = clockwise[direction[num]]
            ny, nx = y + dy, x + dx

        if players[ny][nx] == EMPTY:
            players[ny][nx], players[y][x] = num, EMPTY
            location[num] = (ny, nx)
            get_gun(num)
        else:
            players[y][x] = EMPTY
            fight(num, ny, nx)

def get_gun(num):
    y, x = location[num]
    if len(guns[y][x]) == 0:
        return

    user_gun = power_gun[num][1]
    strong = max(guns[y][x])

    if user_gun == 0:
        power_gun[num][1] = strong
        guns[y][x].remove(strong)
    elif user_gun < strong:
        strong_idx = guns[y][x].index(strong)
        guns[y][x][strong_idx], power_gun[num][1] = user_gun, guns[y][x][strong_idx]


def lose(num, y, x):
    if power_gun[num][1] > 0:
        guns[y][x].append(power_gun[num][1])
    power_gun[num][1] = 0

    for _ in range(4):
        dy, dx = clockwise[direction[num]]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and players[ny][nx] == EMPTY:
            return ny, nx
        direction[num] = (direction[num] + 1) % 4
def change_location(lose_num, ly, lx, win_num, wy, wx):
    old_ly, old_lx = location[lose_num]
    old_wy, old_wx = location[win_num]

    players[old_ly][old_lx], players[old_wy][old_wx] = EMPTY, EMPTY
    players[ly][lx], players[wy][wx] = lose_num, win_num
    location[lose_num], location[win_num] = (ly, lx), (wy, wx)

def win(num, dif):
    point[num] += dif
    y, x = location[num]
    get_gun(num)

def fight(num, y, x):
    num2 = players[y][x]
    sum1 = sum(power_gun[num])
    sum2 = sum(power_gun[num2])

    if sum1 < sum2:
        ly, lx = lose(num, y, x)
        change_location(num, ly, lx, num2, y, x)
        win(num2, sum2 - sum1)
        get_gun(num)
    elif sum1 > sum2:
        ly, lx = lose(num2, y, x)
        change_location(num2, ly, lx, num, y, x)
        win(num, sum1 - sum2)
        get_gun(num2)
    elif power_gun[num][0] > power_gun[num2][0]:
        ly, lx = lose(num2, y, x)
        change_location(num2, ly, lx, num, y, x)
        win(num, sum1-sum2)
        get_gun(num2)
    else:
        ly, lx = lose(num, y, x)
        change_location(num, ly, lx, num2, y, x)
        win(num2, sum2-sum1)
        get_gun(num)

for _ in range(K):
    move()
for p in point[1:]:
    print(p, end=" ")