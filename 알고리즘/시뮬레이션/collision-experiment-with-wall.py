t = int(input())

direct = {
    'U':0,
    'R':1,
    'L':2,
    'D':3,
}
dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]

for _ in range(t):
    n, m = map(int, input().split())
    cball = [[-1 for _ in range(n)] for _ in range(n)]
    for __ in range(m):
        x, y, d = input().split()
        x, y, d = int(x)-1, int(y)-1, direct[d]
        cball[x][y] = d
    for __ in range(2*n):
        nball = [[[] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if cball[i][j]!=-1:
                    d = cball[i][j]
                    nx, ny = i+dx[d], j+dy[d]
                    if not (0<=nx<n and 0<=ny<n):
                        d = 3-d
                        nx, ny = i, j
                    nball[nx][ny].append(d)
        for i in range(n):
            for j in range(n):
                if not nball[i][j] or len(nball[i][j])>=2:
                    cball[i][j] = -1
                else:
                    cball[i][j] = nball[i][j][0]
    answer = 0
    for i in range(n):
        for j in range(n):
            if cball[i][j]!=-1:
                answer += 1
    print(answer)