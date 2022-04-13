n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def getTime(x, y, dir):
    time = 0
    while True:
        time += 1
        nx, ny = x+dx[dir], y+dy[dir]
        if 0<=nx<n and 0<=ny<n:
            x, y = nx, ny
            if board[x][y]==1:
                dir = 1^dir
            elif board[x][y]==2:
                dir = 3-dir
        else:
            break
    return time

answer = 0
for i in range(n):
    answer = max(answer, max([getTime(n, i, 0), getTime(i, -1, 1), getTime(-1, i, 2), getTime(i, n, 3)]))
print(answer)