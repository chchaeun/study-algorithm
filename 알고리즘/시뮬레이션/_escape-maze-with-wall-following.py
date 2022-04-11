import sys; input=sys.stdin.readline
n = int(input().strip())
x, y = map(lambda x: int(x)-1, input().split())
board = [list(input().strip()) for _ in range(n)]

def turn_left(dir):
    return (dir-1+4)%4

def turn_right(dir):
    return (dir+1) % 4


def isPossible(x, y, dir):
    for _ in range(4):
        nx, ny = x+dx[dir], y+dy[dir]
        if not (0<=nx<n and 0<=ny<n):
            return [1000]*3
        elif board[nx][ny]=='.':
            return nx, ny, dir
        dir = turn_left(dir)
    return [-1]*3

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir = 0
time = 0
visited = [[set() for _ in range(n)] for _ in range(n)]
visited[x][y].add(0)
while True:
    time+=1
    x, y, dir = isPossible(x, y, dir)
    if x==1000:
        break
    elif x==-1 or dir in visited[x][y]:
        print(-1)
        exit()
    rx, ry = x+dx[turn_right(dir)], y+dy[turn_right(dir)]
    if 0<=rx<n and 0<=ry<n and board[rx][ry]=='.':
        dir = turn_right(dir)
    visited[x][y].add(dir)
print(time)

# 같은 좌표 같은 방향으로 다시 돌아오면 안됨