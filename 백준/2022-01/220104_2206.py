import sys
from collections import deque


def bfs():
    dq = deque([(0, 0, 0)])
    visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while dq:
        x, y, z = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 갈 수 있고, 방문되지 않았을 때
                # 벽 부쉈는지 여부는 상관 X
                if table[nx][ny]=='0' and visited[nx][ny][z]==-1:
                    visited[nx][ny][z] = visited[x][y][z]+1
                    dq.append((nx, ny, z))
                # 갈 수 없고, 방문되지 않았는데 벽 부술 기회가 한 번 있을 때
                elif z==0 and table[nx][ny] == '1' and visited[nx][ny][1] == -1:
                    visited[nx][ny][1] = visited[x][y][z]+1
                    # 지금부터는 벽 부순 상태
                    dq.append((nx, ny, 1))
                    
    return (visited[n-1][m-1][0], visited[n-1][m-1][1]) 

input = sys.stdin.readline
n, m = map(int, input().split())

table = [list(input().strip()) for _ in range(n)]

result1, result2 = bfs()

if result1 == -1 and result2!=-1:
    print(result2)
elif result1 != -1 and result2 == -1:
    print(result1)
else:
    print(min(result1, result2))