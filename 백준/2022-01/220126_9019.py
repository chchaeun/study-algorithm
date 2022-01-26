import sys; input=sys.stdin.readline
from collections import deque

t = int(input().strip())
registers = [list(map(int, input().split())) for _ in range(t)]

global answer
answer = []

def bfs(start, end):
    dq = deque([(start, "")])
    # visited가 전역이면 안됨
    visited = [0 for _ in range(10000)]
    while dq:
        N, A = dq.popleft()
        D = (N*2)%10000
        S = N-1 if N!=0 else 9999
        # 자릿수가 3자리 이하일 때의 경우를 생각해야 함
        L = N*10 if N<1000 else (N%1000)*10+(N//1000)
        R = (N%10)*1000+(N//10)
        for j, k in zip([D, S, L, R], ['D', 'S', 'L', 'R']):
            if j == end:
                return A+k
            if visited[j]==0:
                dq.append((j, A+k))
                visited[j]=1

for r in registers:
    print(bfs(r[0], r[1]))