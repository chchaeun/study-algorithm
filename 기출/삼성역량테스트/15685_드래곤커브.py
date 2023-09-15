n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]

POINT, EMPTY = 1, 0
board = [[EMPTY for _ in range(101)] for _ in range(101)]

clockwise = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for info in infos:
    stack = []
    x, y, d, g = info
    stack.append(d)

    for i in range(g):
        curve = list(map(lambda x: (x + 1) % 4, reversed(stack)))
        stack.extend(curve)

    board[y][x] = POINT
    sy, sx = y, x
    for s in stack:
        dy, dx = clockwise[s]
        sy, sx = sy+dy, sx+dx
        board[sy][sx] = POINT

answer = 0

square = [(0, 0), (0, 1), (1, 0), (1, 1)]
for x in range(100):
    for y in range(100):
        for s in square:
            dy, dx = s
            if board[y+dy][x+dx] == EMPTY:
                break
        else:
            answer += 1

print(answer)