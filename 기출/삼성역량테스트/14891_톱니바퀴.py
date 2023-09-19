def rotate(wnum, direct):
    if visited[wnum]:
        return
    if direct == CLOCK:
        wheels[wnum] = [wheels[wnum][-1]] + wheels[wnum][:-1]
    if direct == ANTICLOCK:
        wheels[wnum] = wheels[wnum][1:] + [wheels[wnum][0]]
    visited[wnum] = True

    for lwheel in linked[wnum]:
        rotate(lwheel, -direct)

wheels = [list(map(int, list(input()))) for _ in range(4)]
k = int(input())
rotations = [list(map(int, input().split())) for _ in range(k)]
N, S = 0, 1
CLOCK, ANTICLOCK = 1, -1

linked, visited = [], []
for rotation in rotations:
    linked = [[] for _ in range(4)]
    visited = [False for _ in range(4)]

    for i in range(3):
        if (wheels[i][2], wheels[i+1][6]) in [(N,S), (S, N)]:
            linked[i].append(i+1)
            linked[i+1].append(i)
    wnum, direct = rotation
    rotate(wnum-1, direct)

answer = 0
for i in range(4):
    answer += wheels[i][0] * 2**i

print(answer)