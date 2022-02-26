from collections import deque
from copy import deepcopy
import sys; input=sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def melt():
    temp = deepcopy(board)
    for x in range(n):
        for y in range(m):
            if board[x][y]==1:
                count=0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<n and 0<=ny<m and temp[nx][ny]==2:
                        count+=1
                if count>=2:
                    board[x][y]=2
    if temp==board:
        return True
    return False


def outside(a, b):
    dq = deque([(a, b)])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
                dq.append((nx, ny))
                board[nx][ny] = 2
answer = 0
while True:
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                outside(i, j)
    if melt():
        break
    answer+=1
    
print(answer)