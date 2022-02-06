import sys; input=sys.stdin.readline
from collections import deque
from itertools import combinations

def distance(house, chicken):
    dist = 0
    for h in house:
        hdist = 3000
        for c in chicken:
            hdist = min(hdist, abs(h[0]-c[0])+abs(h[1]-c[1]))
        dist += hdist
    return dist
            
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
answer = 250000

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))
            
comb = combinations(chicken, m)

for c in comb:
    answer = min(answer, distance(house, c))
    
print(answer)