import sys; input=sys.stdin.readline
n = int(input().strip())
turn = []
like = [None for _ in range(n*n+1)]
for _ in range(n*n):
    temp = list(map(int, input().split()))
    turn.append(temp[0])
    like[temp[0]] = temp[1:]
board = [[0 for _ in range(n)] for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
nboard = [[0 for _ in range(n)] for _ in range(n)]
def friends(num):
    fmax = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]: continue
            count = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] and board[nx][ny] in like[num]:
                    count += 1
            nboard[i][j] = count
            if fmax < count: fmax = count
    return fmax
                
def empty(fmax):
    emax = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] or nboard[i][j] != fmax: 
                nboard[i][j] = 0
                continue
            count = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
                    count += 1
            nboard[i][j] = count
            if emax < count: emax = count
    return emax

def put(emax, num):
    for i in range(n):
        for j in range(n):
            if not board[i][j] and nboard[i][j]==emax:
                board[i][j] = num
                return
def score():
    _sum = 0
    scores = [0, 1, 10, 100, 1000]
    for i in range(n):
        for j in range(n):
            count = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] in like[board[i][j]]:
                    count += 1
            _sum += scores[count]
    return _sum

for num in turn:
    put(empty(friends(num)), num)
    
print(score())