import sys; input=sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
size = [0 for _ in range(n*m+1)]


def getRectangle(x, y, h, w):
    for i in range(x, x+h):
        for j in range(y, y+w):
            if board[i][j]<=0:
                return False
    return True

def getSize(n, m, h, w):
    for i in range(n-h+1):
        for j in range(m-w+1):
            if getRectangle(i, j, h, w):
                return True
    return False

for i in range(1, n+1):
    for j in range(1, m+1):
        if size[i*j]: continue
        if getSize(n, m, i, j):
            size[i*j] = 1

for i in range(len(size)-1, -1, -1):
    if size[i]:
        print(i)
        break
else: print(-1)