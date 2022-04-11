import sys; input=sys.stdin.readline
n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

def bomb(x, y):
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        i=0
        while i<board[x][y]:
            nx, ny = x+dx*i, y+dy*i
            if 0<=nx<n and 0<=ny<n:
                nboard[nx][ny] = 0
            else:
                break
            i+=1

def drop():
    for j in range(n):
        temp = []
        for i in range(n):
            if nboard[i][j]:
                temp.append(nboard[i][j])
        temp = [0 for _ in range(n-len(temp))] + temp
        for i in range(n):
            nboard[i][j] = temp[i]

def pair():
    dxs, dys = [1, 0], [0, 1]
    count = 0
    for i in range(n):
        for j in range(n):
            if not nboard[i][j]: continue
            for dx, dy in zip(dxs, dys):
                nx, ny = i+dx, j+dy
                if 0<=nx<n and 0<=ny<n and nboard[nx][ny]==nboard[i][j]:
                    count += 1
    return count

nboard = []
answer = 0
for i in range(n):
    for j in range(n):
        nboard = [row[:] for row in board]
        bomb(i, j)
        drop()
        answer = max(pair(), answer)
print(answer)