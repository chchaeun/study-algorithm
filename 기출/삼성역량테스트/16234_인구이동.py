from collections import deque

def in_range(n, y, x):
    return 0<=y<n and 0<=x<n

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

movement = True
while movement:
    movement = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dq = deque([(i, j)])
                dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]
                union = [(i, j)]
                population, num_of_nation = board[i][j], 1
                while dq:
                    y, x = dq.popleft()
                    visited[y][x] = True
                    for dy, dx in zip(dys, dxs):
                        ny, nx = y+dy, x+dx
                        if in_range(n, ny, nx) and not visited[ny][nx] and l <= abs(board[y][x] - board[ny][nx]) <= r:
                            union.append((ny, nx))
                            visited[ny][nx] = True
                            dq.append((ny, nx))
                            population += board[ny][nx]
                            num_of_nation += 1
                if num_of_nation > 1:
                    movement = True
                    new_population = population // num_of_nation
                    for nation in union:
                        y, x = nation
                        board[y][x] = new_population
    if movement:
        answer += 1
print(answer)
