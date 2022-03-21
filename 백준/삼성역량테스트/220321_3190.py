import sys; input=sys.stdin.readline
from collections import defaultdict, deque

n = int(input().strip())
k = int(input().strip())
board = [[0]*(n+1) for _ in range(n+1)]
board[0][0] = 1
for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = 2
l = int(input().strip())

change = defaultdict(lambda: '')
for _ in range(l):
    x, c = input().split()
    change[int(x)] = c
    
# Left, Up, right, Down
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
# L일 때는 dx, dy 인덱스 감소, D일 때는 증가
rotate = {'L': -1, 'D': 1}

cur_direct = 2

snake = deque([(1, 1)])
visited = defaultdict(int)
visited[(1, 1)] = 1

count = 0
while True:
    count += 1
    row, col = snake[0][0] + dx[cur_direct], snake[0][1] + dy[cur_direct]
    if 1<=row<n+1 and 1<=col<n+1 and not visited[(row, col)]:
        if board[row][col] != 2:
            prow, pcol = snake.pop()
            visited[(prow, pcol)] = 0
        else: board[row][col] = 0
        snake.appendleft((row, col))
        visited[(row, col)] = 1;
        if change[count]:
            cur_direct = (cur_direct + rotate[change[count]]) % 4
    else: break

print(count)