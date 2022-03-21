import sys; input=sys.stdin.readline
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

answer = []
dice = [0 for _ in range(6)]

def changeDice(order):
    if order == 1:
        dice[4], dice[1], dice[5], dice[3] = dice[3], dice[4], dice[1], dice[5]
    elif order == 2:
        dice[4], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[4]
    elif order == 3:
        temp = dice[0]
        for i in range(3):
            dice[i] = dice[i+1]
        dice[3] = temp
    else:
        temp = dice[3]
        for i in range(3, 0, -1):
            dice[i] = dice[i-1]
        dice[0] = temp

def move(order, x, y):
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    nx, ny = x+dx[order], y+dy[order]
    if 0<=nx<n and 0<=ny<m:
        changeDice(order)
        if board[nx][ny]==0:
            board[nx][ny]=dice[3]
        else:
            dice[3] = board[nx][ny]
            board[nx][ny] = 0
        answer.append(dice[1])
        return nx, ny
    else: return x, y
    
for i in order:
    x, y = move(i, x, y)

for a in answer:
    print(a)