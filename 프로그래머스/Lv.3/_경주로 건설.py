from collections import deque

def solution(board):
    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    EMPTY, WALL = 0, 1
    STRAIT, CORNER = 100, 500
    INF = int(1e9)
    N = len(board)

    cost = [[[INF for _ in range(4)] for _ in range(N)] for _ in range(N)]
    for i in range(4):
        cost[0][0][i] = 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dq = deque([(0, 0, d) for d in range(4)])

    while dq:
        y, x, d = dq.popleft()

        for i, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx

            new_cost = cost[y][x][d] + (STRAIT if i == d else STRAIT + CORNER)

            if in_range(ny, nx) and board[ny][nx] != WALL and cost[ny][nx][i] > new_cost:
                cost[ny][nx][i] = new_cost

                if ny == N-1 and nx == N-1:
                    continue

                dq.append((ny, nx, i))

    return min(cost[N-1][N-1])

solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])