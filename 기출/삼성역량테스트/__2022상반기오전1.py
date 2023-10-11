# 코드트리 술래잡기
from collections import defaultdict
global police, thief
n, m, h, k = map(int, input().split())
thief = defaultdict(list)
tree = defaultdict(bool)
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
police = [[n//2 + 1, n//2 + 1], 0]

for _ in range(m):
    y, x, d = map(int, input().split())
    thief[(y, x)].append(d)

for _ in range(h):
    y, x = map(int, input().split())
    tree[(y, x)] = True

def thief_move():
    thiefs = list(thief.items()).copy()
    new_thief = defaultdict(list)
    for pos, dirs in thiefs:
        ty, tx = pos
        py, px = police[0]

        move_done = []
        for dir in dirs:
            if dir in move_done:
                continue

            dy, dx = direction[dir]
            ny, nx = ty + dy, tx + dx

            count = dirs.count(dir)
            if abs(py-ty) + abs(px-tx) <= 3:
                if 1 <= ny <= n and 1 <= nx <= n:
                    if ny == py and nx == px:
                        for _ in range(count):
                            new_thief[(ty, tx)].append(dir)
                        move_done.append(dir)
                    else:
                        for _ in range(count):
                            new_thief[(ny, nx)].append(dir)
                        move_done.append(dir)

                else:
                    dy, dx = direction[(dir + 2)%4]
                    ny, nx = ty + dy, tx + dx

                    if ny == py and nx == px:                        
                        for _ in range(count):
                            new_thief[(ty, tx)].append((dir+2) % 4)                        
                        move_done.append(dir)
                    else:
                        for _ in range(count):
                            new_thief[(ny, nx)].append((dir+2) % 4)
                        move_done.append(dir)
            else:
                for _ in range(count):
                    new_thief[(ty, tx)].append(dir)
                move_done.append(dir)


    return new_thief

global answer
answer = 0

def catch():
    global answer, turn, thief
    (y, x), d = police
    print('turn ', turn)
    print(y, x, d)
    dy, dx = direction[d]
    for i in range(3):
        ny, nx = y + dy * i, x + dx * i
        if not (1<=ny<=n and 1<=nx<=n) or tree[(ny, nx)]:
            continue
        answer += len(thief[(ny, nx)]) * turn
        thief[(ny, nx)] = []
    
    turn += 1
    thief = thief_move()

    if turn > k:
        print(answer)
        exit()

def outside():
    global police

    y, x, d = n//2, n//2+1, 1
    unit = 1
    while True:
        for _ in range(2 if unit != 1 else 1):
            for __ in range(unit):
                if (y, x) == (1, 1):
                    return
                police = [(y, x), d]
                catch()
                # way.append((y, x, d))
                dy, dx = direction[d]
                ny, nx = y + dy, x + dx

                y, x = ny, nx
            d = (d+1) % 4
        unit += 1

def inside():
    global police

    y, x, d = 1, 1, 2
    unit = 4
    while True:
        for _ in range(2 if unit < 4 else 3):
            for __ in range(unit):
                police = [(y, x), d]
                catch()
                # way.append((y, x, d))
                dy, dx = direction[d]
                ny, nx = y + dy, x + dx
                y, x = ny, nx
                if (y, x) == (n//2+1, n//2+1):
                    police = [(n//2+1, n//2+1), 0]
                    catch()
                    return
            d = (d-1) % 4
        unit -= 1

    
way = []
i = 1
global turn
turn = 1
length = len(way)

thief = thief_move()
while turn <= k:
    # y, x, d = way[i % length]
    # police = [(y, x), d]
    # catch(turn)
    outside()
    inside()
    # i += 1
    # turn += 1

# print(answer)


# direction_shape = ['위', '오', '아', '왼']
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == police[0][0] and j == police[0][1]:
#             print("술", end="")
#         elif len(thief[(i, j)])>0:
#             print('(', end="")
#             for t in thief[(i, j)]:
#                 print(direction_shape[t], end="")
#             print(')', end="")

#         else:
#             print("빈", end="")
#     print()
# print()
