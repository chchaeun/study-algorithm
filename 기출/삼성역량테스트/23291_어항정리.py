from collections import defaultdict, deque

EMPTY = 0
N, K = map(int, input().split())
bowl = list(map(int, input().split()))

def add_fish():
    _min = int(1e9)
    min_index = []
    for i, b in enumerate(bowl):
        if _min > b:
            _min = b
            min_index = [i]
        elif _min == b:
            min_index.append(i)

    for mi in min_index:
        bowl[mi] += 1

def rotate_1(bowl):
    fish = defaultdict(int)
    for i, b in enumerate(bowl):
        fish[(N-1, i)] = b

    h, w = 1, 1
    turn = 1
    y, x = N-1, 0
    while True:
        for i in range(w):
            for j in range(h):
                fish[(y-w+i, x+w+j)] = fish[(y-j, x+i)]
                fish[(y-j, x+i)] = EMPTY
        x += w

        if turn % 2 == 0:
            w += 1
        else:
            h += 1
        turn += 1
        if h > N-h*w:
            break
    
    return fish

def move(fish):
    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
    moving = defaultdict(int)
    keys = list(fish.keys()).copy()
    for key in keys:
        if fish[key] == EMPTY:
            continue
        y, x = key

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and fish[(ny, nx)] != EMPTY and fish[(y, x)] > fish[(ny, nx)]:
                d = (fish[(y, x)] - fish[(ny, nx)]) // 5
                if d > 0:
                    moving[(y, x)] -= d
                    moving[(ny, nx)] += d
  
    for key in fish.keys():
        fish[key] += moving[key]
    
    return fish

def one_line(fish):
    line = []
    for key in sorted(list(fish.keys()), key=lambda x: (x[1], -x[0])):
        if fish[key] != EMPTY:
            line.append(fish[key])
    
    return line

def rotate_2():
    new_fish = defaultdict(int)
    for i, b in enumerate(bowl):
        new_fish[(3, i)] = b

    half = N//2
    for i in range(half):
        print((3, half - 1 - i), (2, half + i))
        new_fish[(2, half + i)] = new_fish[(3, half - 1 - i)]
        new_fish[(3, half - 1 - i)] = EMPTY

    hoh = N//4
    for i in range(3, 1, -1):
        for j in range(hoh):
            new_fish[(3-i, N-hoh+j)] = new_fish[(i, N - hoh - 1 - j)]
            new_fish[(i, N - hoh - 1 - j)] = EMPTY
            
    return new_fish

answer = 0
while max(bowl) - min(bowl) > K:
    add_fish()
    fish = rotate_1(bowl)
    fish = move(fish)
    bowl = one_line(fish)
    fish = rotate_2()
    fish = move(fish)
    bowl = one_line(fish)
    answer += 1

print(answer)
