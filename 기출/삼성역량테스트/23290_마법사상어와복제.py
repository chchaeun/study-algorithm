from collections import defaultdict
M, S = map(int, input().split())

global shark, fish, smell
fish = defaultdict(list)
smell = defaultdict(int)
direction_8 = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
direction_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(M):
    y, x, d = map(int, input().split())
    fish[(y, x)].append(d-1)

shark = list(map(int, input().split()))

def move_fish():
    global fish
    new_fish = defaultdict(list)
    for loc, dlist in fish.items():
        move_done = []
        y, x = loc
        for d in dlist:
            if d in move_done:
                continue

            move_success = False

            for i in range(8):
                dy, dx = direction_8[(d-i) % 8]
                ny, nx = y + dy, x + dx

                if 1 <= ny < 5 and 1 <= nx < 5 and [ny, nx] != shark and smell[(ny, nx)] == 0:
                    for _ in range(dlist.count(d)):
                        new_fish[(ny, nx)].append((d-i) % 8)
                    move_done.append(d)
                    move_success = True
                    break

            if not move_success:
                for _ in range(dlist.count(d)):
                    new_fish[(y, x)].append(d)
                move_done.append(d)

    fish = new_fish

def move_shark_case(arr, total, sy, sx):
    global max_arr, _max
    if len(arr) == 3:
        if _max <= total:
            max_arr = arr.copy()
            _max = total
        return
    for i in range(3, -1, -1):
        dy, dx = direction_4[i]
        ny, nx = sy + dy, sx + dx
        if 1 <= ny < 5 and 1 <= nx < 5:
            numoffish = 0 if (ny, nx) in arr else len(fish[(ny, nx)])
            arr.append((ny, nx))
            move_shark_case(arr, total + numoffish, ny, nx)
            arr.pop()
def move_shark():
    eated = []
    global shark, smell
    for ny, nx in max_arr:
        if len(fish[(ny, nx)]) > 0 and (ny, nx) not in eated:
            smell[(ny, nx)] = 3
            fish[(ny, nx)] = []
            eated.append((ny, nx))
        
        shark = [ny, nx]

def remove_smell():
    for key in smell.keys():
        if smell[key] > 0:
            smell[key] -= 1

def copy_done():
    for key, element in copy_fish.items():
        fish[key].extend(element)

for _ in range(S):
    copy_fish = defaultdict(list)
    for key, element in fish.items():
        copy_fish[key] = element.copy()

    move_fish()

    global max_arr, _max
    max_arr = []
    _max = 0

    move_shark_case([], 0, shark[0], shark[1])
    
    move_shark()

    remove_smell()

    copy_done()

answer = 0
for f in fish.values():
    answer += len(f)
print(answer)