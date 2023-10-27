from collections import defaultdict

EMPTY, WALL = 0, -1
N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

tree = defaultdict(int)
poison = defaultdict(int)
wall = defaultdict(bool)

for i in range(N):
    for j in range(N):
        if board[i][j] == WALL:
            wall[(i, j)] = True
        if board[i][j] > 0:
            tree[(i, j)] = board[i][j]

def add(new_tree):
    for (y, x), num in new_tree.items():
        tree[(y, x)] += num

dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
def grow_spread():
    grow_tree = defaultdict(int)
    spread_tree = defaultdict(int)
    spread_point = defaultdict(list)
    trees = list(tree.keys()).copy()
    for y, x in trees:
        if tree[(y, x)] == 0:
            continue
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if tree[(ny, nx)] > 0:
                    grow_tree[(y, x)] += 1
                if tree[(ny, nx)] == 0 and not wall[(ny, nx)] and poison[(ny, nx)] == 0:
                    spread_point[(y, x)].append((ny, nx))

    add(grow_tree)

    for (y, x), points in spread_point.items():
        for ny, nx in points:
            spread_tree[(ny, nx)] += tree[(y, x)] // len(points)

    add(spread_tree)

dia_dys, dia_dxs = [-1, -1, 1, 1], [-1, 1, -1, 1]

global answer
answer = 0

def find_max():
    global answer

    _max, max_point = 0, (-1, -1)
    trees = list(tree.keys()).copy()
    for y, x in trees:
        if tree[(y, x)] == 0:
            continue
        count = tree[(y, x)]
        for dy, dx in zip(dia_dys, dia_dxs):
            for k in range(1, K+1):
                ny, nx = y + dy * k, x + dx * k
                if 0 <= ny < N and 0 <= nx < N:
                    if wall[(ny, nx)] or tree[(ny, nx)] == 0:
                        break
                    count += tree[(ny, nx)]
        if count > _max or count == _max and max_point > (y, x):
            _max = count
            max_point = (y, x)

    answer += _max
    return max_point

def remove():
    y, x = find_max()
    poison[(y, x)] = C + 1
    new_tree = defaultdict(int)
    new_tree[(y, x)] -= tree[(y, x)]

    for dy, dx in zip(dia_dys, dia_dxs):
        for k in range(1, K + 1):
            ny, nx = y + dy * k, x + dx * k
            if 0 <= ny < N and 0 <= nx < N:
                poison[(ny, nx)] = C + 1
                new_tree[(ny, nx)] -= tree[(ny, nx)]
                if wall[(ny, nx)] or tree[(ny, nx)] == 0:
                    break
    add(new_tree)
def disappear_poison():
    for y, x in poison.keys():
        if poison[(y, x)] > 0:
            poison[(y, x)] -= 1

import time
st = time.time()

for _ in range(M):
    grow_spread()
    remove()
    disappear_poison()
    #
    # for i in range(N):
    #     for j in range(N):
    #         if tree[(i, j)] > 0:
    #             print(tree[(i, j)], end=" ")
    #         elif poison[(i, j)] >0:
    #             print("독", end=" ")
    #         elif wall[(i, j)]:
    #             print("벽", end=" ")
    #         else:
    #             print(0, end=" ")
    #     print()
    # print()

print(answer)

et = time.time()
print(et-st)