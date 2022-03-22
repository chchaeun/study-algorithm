from copy import deepcopy
import sys; input=sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def gold_mining(x, y, k):
    return (sum([board[i][j] if abs(x-i)+abs(y-j)<=k else 0 for j in range(n) for i in range(n)]))
global gold 
answer = 0
visited = []
for k in range(n):
    cost = k*k + (k+1)*(k+1)
    for i in range(n):
        for j in range(n):
            gold = gold_mining(i, j, k)
            if m*gold-cost>=0:
                answer = max(answer, gold)
print(answer)
