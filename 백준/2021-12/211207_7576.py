import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dq = deque()
for i in range(n):
    for j in range(m):
        if table[i][j]==1:
            dq.append((i, j))


def bfs():
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if table[nx][ny] == 0: 
                table[nx][ny] = table[x][y]+1
                dq.append((nx, ny))
 
bfs()                
         
result = 0
for i in table:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
        result = max(result, j-1)

print(result)

# 다른 시작점 두 개에 시작하면 visited 여러 번 초기화해서 사용하지 않아도 됨
# 처음엔 하루마다 count+=1을 해주기 위해서 level이라는 queue를 사용해서 호출 레벨을 구분하려고 했는데 그렇게 하면 굉장히 복잡함
# 호출레벨마다 같은 숫자로 table을 업데이트 해주면 됨
# 결국 최단경로 찾는 문제처럼 풀면 됨