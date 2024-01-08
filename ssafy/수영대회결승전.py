from collections import defaultdict

WATER, LAND, TORNADO = 0, 1, 2
INF = int(1e9)

T = int(input())

for case in range(1, T+1):
    N = int(input())
    sea = [list(map(int, input().split())) for _ in range(N)]
    tornado = []
    for i in range(N):
        for j in range(N):
            if sea[i][j] == TORNADO:
                tornado.append((i, j))


    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]

    visited = defaultdict(bool)
    visited[(sy, sx)] = True

    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    def toggle_tornado():
        for ty, tx in tornado:
            sea[ty][tx] = WATER if sea[ty][tx] == TORNADO else TORNADO

    time = 1
    answer = INF

    while time < N * (N + 2):
        visited_points = list(visited.keys())
        for point in visited_points:
            if not visited[point]:
                continue
            y, x = point
            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx

                if in_range(ny, nx) and sea[ny][nx] == WATER:
                    visited[(ny, nx)] = True
                
                if ny == gy and nx == gx:
                    answer = min(answer, time)
        
        time += 1

        if (time - 1) % 3 == 0 and time != 1 or time % 3 == 0:
            toggle_tornado()

    print("#{} {}".format(case, -1 if answer == INF else answer))