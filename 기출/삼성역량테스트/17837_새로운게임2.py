from collections import deque, defaultdict

WHITE, RED, BLUE = 0, 1, 2
DIRECTION = {
    1: (0, 1), 
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

N, K = map(int, input().split())
board_color = [list(map(int, input().split())) for _ in range(N)]
board_dq = [[deque() for _ in range(N)] for _ in range(N)]
location = defaultdict(list)

for i in range(K):
    y, x, d = map(int, input().split())
    location[i+1] = [y-1, x-1, d]
    board_dq[y-1][x-1].append(i+1)

def move(num):
    y, x, d = location[num]
    ny, nx = y + DIRECTION[d][0], x + DIRECTION[d][1]

    if not (0 <= ny < N and 0 <= nx < N) or board_color[ny][nx] == BLUE:
        reverse = d-1 if d % 2 == 0 else d+1
        ny, nx, d = y + DIRECTION[reverse][0], x + DIRECTION[reverse][1], reverse
        location[num][2] = reverse

    if not (0 <= ny < N and 0 <= nx < N) or board_color[ny][nx] == BLUE:
        return False

    for i, el in enumerate(board_dq[y][x]):
        if el == num:
            index = i
    length = len(board_dq[y][x])
    move_list = [board_dq[y][x].pop() for _ in range(length - index)]

    if board_color[ny][nx] == WHITE:
        move_list.reverse()

    for ml in move_list:
        location[ml] = [ny, nx, location[ml][2]]
        board_dq[ny][nx].append(ml)

    if len(board_dq[ny][nx]) >= 4:
        return True

    return False

turn = 0
breaker = False
while turn <= 1000 and not breaker:
    turn += 1
    for i in range(1, K+1):
        breaker = move(i)
        if breaker:
            break
        
if turn > 1000:
    print(-1)
else:
    print(turn)