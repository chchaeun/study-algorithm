from collections import deque

CLOCKWISE, ANTICLOCKWISE = 0, 1

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def rotate(x, d, k):
    startx = x
    while x-1 < N:
        if d == CLOCKWISE:
            board[x-1] = board[x-1][M-k:] + board[x-1][:M-k]
        if d == ANTICLOCKWISE:
            board[x-1] = board[x-1][k:] + board[x-1][:k]
        x += startx

def in_range(y, x):
    return 0 <= y < N and 0 <= x < M

def erase():
    success = False
    dys, dxs = [1, -1, 0, 0], [0, 0, 1, -1]
    for sy in range(N):
        for sx in range(M):
            standard = board[sy][sx]
            
            if standard == 0:
                continue

            dq = deque([(sy, sx)])
            visited = [[False for _ in range(M)] for _ in range(N)]
            visited[sy][sx] = True
            
            while dq:
                y, x = dq.popleft()
                for index, (dy, dx) in enumerate(zip(dys, dxs)):
                    ny, nx = y + dy, x + dx
                    if index > 1:
                        nx %= M

                    if in_range(ny, nx) and not visited[ny][nx] and standard == board[ny][nx]:
                        dq.append((ny, nx))
                        visited[ny][nx] = True
                        board[y][x] = 0
                        board[ny][nx] = 0
                        success = True
    return success


def sum_avg():
    _sum = 0
    count = 0
    for b in board:
        for el in b:
            if el == 0:
                continue
            count += 1
            _sum += el
    if count == 0:
        return (0, 0)
    return (_sum, _sum / count)

def average():
    avg = sum_avg()[1]
    
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                continue
            if board[y][x] > avg:
                board[y][x] -= 1
            elif board[y][x] < avg:
                board[y][x] += 1
            
for i in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)

    if not erase():
        average()
        
print(sum_avg()[0])