from collections import defaultdict, deque
import heapq
import sys; input=sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def getFish(x, y, eat, shark):
    global answer
    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]
    dq = deque([(x, y, 0)])
    while dq:
        cx, cy, dist = dq.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            ndist = dist + 1
            if 0<=nx<n and 0<=ny<n and (nx, ny)!=(x, y):
                if not board[nx][ny] or shark == board[nx][ny]:
                    dq.append((nx, ny, ndist))
                elif board[nx][ny] and board[nx][ny]<shark:
                    answer += ndist
                    board[x][y], board[nx][ny] = 0, 9
                    del fish[(nx, ny)]
                    if eat+1==shark:
                        return nx, ny, 0, shark+1
                    else: return nx, ny, eat+1, shark
                
x, y = 0, 0
fish = defaultdict(int)
for i in range(n):
    for j in range(n):
        if board[i][j] and board[i][j]!=9:
            fish[(i, j)] = board[i][j]
        elif board[i][j]==9:
            x, y = i, j
            
 
global answer
answer = 0
eat = 0
shark = 2
while fish and shark>min(fish.values()):
    x, y, eat, shark = getFish(x, y, eat, shark)
    print()
    for b in board:
        print(*b)
    print(x, y, answer)
    
print(answer)