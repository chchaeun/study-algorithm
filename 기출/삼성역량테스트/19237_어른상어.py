N, M, K = map(int, input().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
EMPTY = 0
number = [[EMPTY for _ in range(N)] for _ in range(N)]
time = [[0 for _ in range(N)] for _ in range(N)]
shark = [[] for _ in range(M+1)]
shark_board = [[EMPTY for _ in range(N)] for _ in range(N)]
priority = [[] for _ in range(M+1)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 0:
            continue
        shark[temp[j]] = [i, j, -1]
        shark_board[i][j] = temp[j]
        number[i][j] = temp[j]
        time[i][j] = K

for i, d in enumerate(list(map(int, input().split()))):
    shark[i+1][2] = d-1

for i in range(M*4):
    temp = list(map(lambda x: int(x) - 1, input().split()))
    priority[i//4+1].append(temp)

def move():
    for i in range(M, 0, -1):
        if not shark[i]:
            continue

        y, x, d = shark[i]
        no_smell, my_smell = [], []
        for p in priority[i][d]:
            dy, dx = direction[p]
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if number[ny][nx] == 0:
                    no_smell.append((ny, nx, p))
                if number[ny][nx] == i:
                    my_smell.append((ny, nx, p))

        if no_smell:
            ny, nx, nd = no_smell[0]
        elif my_smell:
            ny, nx, nd = my_smell[0]
        else:
            continue

        shark[i] = [ny, nx, nd]
        if shark_board[ny][nx]:
            shark[shark_board[ny][nx]] = []

        shark_board[ny][nx], shark_board[y][x] = i, EMPTY

def smell():
    for i in range(N):
        for j in range(N):
            if shark_board[i][j] != EMPTY:
                number[i][j] = shark_board[i][j]
                time[i][j] = K
            if shark_board[i][j] == EMPTY and time[i][j] > 0:
                time[i][j] -= 1
            if time[i][j] == 0:
                number[i][j] = EMPTY

answer = 0
flag = True

while answer < 1001 and flag:
    flag = False

    move()
    smell()
    
    for s in shark[2:]:
        if len(s)>0:
            flag = True

    answer += 1

answer = -1 if answer==1001 else answer

print(answer)
