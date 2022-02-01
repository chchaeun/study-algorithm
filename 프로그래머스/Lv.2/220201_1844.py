from collections import deque
def solution(maps):
    answer = bfs(0, 0, maps)
    if answer == 1: return -1
    return answer

def bfs(a, b, maps):
    n, m = len(maps), len(maps[0])
    dq = deque([(a, b)])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while dq:
        x, y = dq.popleft()
        for i, j in zip(dx, dy):
            nx, ny = x+i, y+j
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]==1 or maps[nx][ny]>maps[x][y]+1:
                    dq.append((nx, ny))
                    maps[nx][ny] = maps[x][y]+1
    return maps[n-1][m-1]


for test in [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]], [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]:
    print(solution(test))