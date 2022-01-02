# pypy3로 실행해야 시간초과 안남
# 반복 작업이 많아서 캐싱해주기 때문

import sys, copy
from collections import deque

input = sys.stdin.readline

# 벽 세우기(재귀)
def wall(cnt):
    # 세 개 다 세우면 virus 퍼뜨리고 return
    if cnt == 3:
        virus()
        return
    # table 돌면서 0이면 벽 세우고 wall 호출
    # return 돼서 돌아오면 원래대로 돌림
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                table[i][j] = 1
                wall(cnt+1)
                table[i][j] = 0

# virus 퍼뜨리는 함수(bfs)
def virus():
    global result
    # 깊은 복사 해줘야 오류 X
    # 슬라이싱으로 복사해도 오류 남
    # for문으로 하나하나 넣어도 됨
    temp = copy.deepcopy(table)
    dq = deque()
    for i in range(n):
        for j in range(m):
            if table[i][j]==2:
                dq.append((i, j))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            b = y+dy[i]
            a = x+dx[i]
            if 0<=a<m and 0<=b<n and temp[b][a]==0:
                dq.append((b, a))
                temp[b][a] = 2
    count=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                count+=1
    result = max(count, result)
    
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

result=0

wall(0)

print(result)
