from collections import defaultdict, deque
import sys; input=sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def getFish(x, y, eat, shark):
    global answer
    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]
    dq = deque([(0, x, y)])
    visited = defaultdict(int)
    visited[(x, y)] = 1
    while dq:
        cdist, cx, cy = dq.popleft()
        if (x, y)!=(cx, cy) and board[cx][cy] and board[cx][cy]<shark:
            answer += cdist
            board[x][y], board[cx][cy] = 0, 9
            if eat+1==shark:
                return cx, cy, 0, shark+1
            else: return cx, cy, eat+1, shark
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            ndist = cdist + 1
            if 0<=nx<n and 0<=ny<n and not visited[(nx, ny)]:
                if shark >= board[nx][ny]:
                    dq.append((ndist, nx, ny))
                    visited[(nx, ny)] = 1
        if dq and dq[0]!=cdist:
            dq = deque(sorted(dq))
    return 0, 0, 0, 0
        
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            x, y = i, j
            
 
global answer
answer = 0
eat = 0
shark = 2
while shark!=0:
    x, y, eat, shark = getFish(x, y, eat, shark)
    
print(answer)