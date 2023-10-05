from collections import deque
import heapq

EMPTY, WALL = 0, 1
BOARD, POINT = 'BOARD', 'POINT'
N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(lambda x: int(x)-1, input().split()))
user_dist = []
user_location = []
dest_location = []

all_distance  = [[None for _ in range(N)] for _ in range(N)]

def distance(sy, sx):
    dboard = [[int(1e9) for _ in range(N)] for _ in range(N)]
    dboard[sy][sx] = 0
    
    dys, dxs = [1, 0, -1, 0], [0, -1, 0, 1]
    dq = deque([(sy, sx)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sy][sx] = True

    while dq:
        y, x = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != WALL and not visited[ny][nx] and dboard[ny][nx] > dboard[y][x] + 1:
                dq.append((ny, nx))
                visited[ny][nx] = True
                dboard[ny][nx] = dboard[y][x] + 1

    return dboard

def near_user(): 
    hq = []

    for i, ul in enumerate(user_location):
        if i in success:
            continue
        uy, ux = ul
        ty, tx = taxi
        
        heapq.heappush(hq, [all_distance[ty][tx][uy][ux], uy, ux, i])

    return heapq.heappop(hq)


for i in range(N):
    for j in range(N):
        all_distance[i][j] = distance(i, j)


for _ in range(M):
    sy, sx, ey, ex = map(lambda x: int(x)-1, input().split())
    user_dist.append(all_distance[sy][sx][ey][ex])
    user_location.append((sy, sx))
    dest_location.append((ey, ex))

success = []
while len(success) < M:
    udist, uy, ux, index = near_user()

    if fuel < udist:
        break

    fuel -= udist

    dy, dx = dest_location[index]
    ddist = all_distance[uy][ux][dy][dx]
    
    if fuel < ddist:
        break

    fuel += ddist
    taxi = [dy, dx]

    success.append(index)

if len(success) == M:
    print(fuel)
else:
    print(-1)