from collections import deque

N, M, K = map(int, input().split())
food = [[5 for _ in range(N)] for _ in range(N)]
tree = [[deque([]) for _ in range(N)] for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    y, x, age = map(int, input().split())
    tree[y-1][x-1].append(age)

def spring_summer():
    for i in range(N):
        for j in range(N):
            death = None
            for idx, t in enumerate(tree[i][j]):
                if food[i][j] >= t:
                    tree[i][j][idx] += 1
                    food[i][j] -= t
                else:
                    death = idx
                    break
            if death is None:
                continue
            for _ in range(len(tree[i][j]) - death):
                death_amount = tree[i][j].pop()
                food[i][j] += death_amount // 2

def fall_winter():
    dys, dxs = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            count = 0
            for idx, t in enumerate(tree[i][j]):
                if t % 5 == 0:
                    count += 1
            for dy, dx in zip(dys, dxs):
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < N:
                    for _ in range(count):
                        tree[ny][nx].appendleft(1)
            food[i][j] += A[i][j]

for _ in range(K):
    spring_summer()
    fall_winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)