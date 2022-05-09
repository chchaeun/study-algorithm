from collections import defaultdict, Counter
import sys; input=sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]
point = []
bombed = defaultdict(int)
global answer
answer = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            point.append((i, j))
            bombed[(i, j)] += 1

cases = [
        [(-2, 0), (-1, 0), (1, 0), (2, 0)],
        [(1, 0), (-1, 0), (0, 1), (0, -1)],
        [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    ]
def bomb(count, case, reset):
    x, y = point[count]
    for c in cases[case]:
        nx, ny = x+c[0], y+c[1]
        if 0<=nx<n and 0<=ny<n:
            bombed[(nx, ny)]+=reset

def choose(count):
    global answer
    
    if len(point) == count:
        temp = 0
        for b in bombed.values():
            if b: temp += 1
        answer = max(answer, temp)
        return
    
    for i in range(3):
        bomb(count, i, 1)
        choose(count + 1)
        bomb(count, i, -1)
        
choose(0)
print(answer)