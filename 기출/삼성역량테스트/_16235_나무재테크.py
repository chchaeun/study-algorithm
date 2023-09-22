from collections import deque

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
land = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    y, x, z = map(int, input().split())
    land[y-1][x-1].append(z)

nutrient = [[5 for _ in range(n)] for _ in range(n)]

def spring_summer():
    for y in range(n):
        for x in range(n):
            new_trees = deque()
            dead_nutrient = 0
            for age in land[y][x]:
                if nutrient[y][x] >= age:
                    nutrient[y][x] -= age
                    new_trees.append(age + 1)
                    continue
                dead_nutrient += age // 2
            land[y][x] = new_trees
            nutrient[y][x] += dead_nutrient

def autumn_winter():
    dys, dxs = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    new_trees = []

    for y in range(n):
        for x in range(n):
            for age in land[y][x]:
                if age % 5 == 0:
                    for dy, dx in zip(dys, dxs):
                        ny, nx = y + dy, x + dx
                        if 0<=ny<n and 0<=nx<n:
                            new_trees.append((ny, nx))
            nutrient[y][x] += a[y][x]
    
    for pos in new_trees:
        y, x = pos
        land[y][x].appendleft(1)

for _ in range(k):
    spring_summer()
    autumn_winter()

answer = 0
for y in range(n):
    for x in range(n):
        answer += len(land[y][x])

print(answer)