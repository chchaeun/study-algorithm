from collections import deque

def solution(land):
    answer = 0

    oil_amount = []
    row_group = [set() for _ in range(len(land[0]))]

    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]

    def in_range(y, x):
        return 0 <= y < len(land) and 0 <= x < len(land[0])

    def bfs(sy, sx):
        if land[sy][sx] == 0 or visited[sy][sx]:
            return
        
        dq = deque([(sy, sx)])
        visited[sy][sx] = True
        count = 0
        
        while dq:
            y, x = dq.popleft()
            count += 1
            row_group[x].add(len(oil_amount))

            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx

                if in_range(ny, nx) and not visited[ny][nx] and land[ny][nx] == 1:
                    dq.append((ny, nx))
                    visited[ny][nx] = True

        oil_amount.append(count)

    for i in range(len(land)):
        for j in range(len(land[i])):
            bfs(i, j)
    
    for row in row_group:
        amount = 0
        for group in row:
            amount += oil_amount[group]

        answer = max(amount, answer)

    return answer

solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])
solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])