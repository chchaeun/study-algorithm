from collections import defaultdict

EMPTY = -1
N, M, K = map(int, input().split()) # N: 격자, M: 플레이어, K: 라운드
clockwise = [(-1, 0), (0, 1), (1, 0), (0, -1)]

location = [None for _ in range(M)]
direction = [None for _ in range(M)]
point = [0 for _ in range(M)]
power_gun = [[None, 0] for _ in range(M)]

gun_board = defaultdict(list)
loc_board = defaultdict(lambda: EMPTY)

for i in range(N):
    guns = list(map(int, input().split()))
    for j in range(N):
        if guns[j] > 0:
            gun_board[(i, j)].append(guns[j])

for num in range(M):
    y, x, d, s = map(int, input().split())
    location[num] = (y-1, x-1)
    loc_board[(y-1, x-1)] = num
    direction[num] = d
    power_gun[num] = [s, 0]

def move(num):
    y, x = location[num]
    dy, dx = clockwise[direction[num]]
    ny, nx = y + dy, x + dx

    if not (0 <= ny < N and 0 <= nx < N):
        direction[num] = (direction[num] + 2) % 4
        dy, dx = clockwise[direction[num]]
        ny, nx = y + dy, x + dx

    # print(num, ny, nx)
    if loc_board[(ny, nx)] == EMPTY:
        location[num] = (ny, nx)
        loc_board[(ny, nx)], loc_board[(y, x)] = num, EMPTY
        get_gun(num)
    else:
        loc_board[(y, x)] = EMPTY
        fight(num, ny, nx)

def get_gun(num):
    y, x = location[num]
    my_gun = power_gun[num][1]

    if len(gun_board[(y, x)]) == 0:
        return

    max_gun = max(gun_board[(y, x)])

    if my_gun < max_gun:
        gun_board[(y, x)].remove(max_gun)
        power_gun[num][1] = max_gun

        if my_gun > 0:
            gun_board[(y, x)].append(my_gun)

def lose(num, y, x):
    # print("lose", y, x)
    if power_gun[num][1] > 0:
        gun_board[(y, x)].append(power_gun[num][1])
        power_gun[num][1] = 0

    for _ in range(4):
        dy, dx = clockwise[direction[num]]
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < N and loc_board[(ny, nx)] == EMPTY:
            location[num] = (ny, nx)
            loc_board[(ny, nx)] = num
            break

        direction[num] = (direction[num] + 1) % 4

    get_gun(num)

def win(num, y, x, dif):
    point[num] += dif
    location[num] = (y, x)
    loc_board[(y, x)] = num
    get_gun(num)

def fight(visit, y, x):
    origin = loc_board[(y, x)]
    sum_visit = sum(power_gun[visit])
    sum_origin = sum(power_gun[origin])
    # print('fight')
    if sum_visit < sum_origin:
        lose(visit, y, x)
        win(origin, y, x, sum_origin - sum_visit)
    elif sum_visit > sum_origin:
        lose(origin, y, x)
        win(visit, y, x, sum_visit - sum_origin)
    elif power_gun[visit][0] > power_gun[origin][0]:
        lose(origin, y, x)
        win(visit, y, x, 0)
    else:
        lose(visit, y, x)
        win(origin, y, x, 0)

# for i in range(N):
#     for j in range(N):
#         print(loc_board[(i, j)], end=" ")
#     print()

for _ in range(K):
    for num in range(M):
        move(num)

# for i in range(N):
#     for j in range(N):
#         print(loc_board[(i, j)], end=" ")
#     print()
# print(power_gun)

# print(direction)
# print(gun_board)
# print(power_gun)

for p in point:
    print(p, end=" ")