import sys; input=sys.stdin.readline
from itertools import product

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
cctv = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]]
}

def getWatch(x, y):
    watch = []
    for direct in cctv[board[x][y]]:
        temp = set()
        for cur in direct:
            cx, cy = x, y
            while True:
                nx, ny = cx+dx[cur], cy+dy[cur]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=6:
                    if not board[nx][ny]:
                        temp.add((nx, ny))
                    cx, cy = nx, ny
                else: break
        watch.append(temp)
    return watch

case = []
zero = 0
for i in range(n):
    for j in range(m):
        if board[i][j] and board[i][j]!=6:
            case.append(getWatch(i, j))
        elif not board[i][j]:
            zero += 1
answer = 100
for prod in product(*case):
    watch = set()
    for p in prod:
        watch |= p
    answer = min(zero-len(watch), answer)
print(answer)