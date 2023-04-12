import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def dfs(y, x):
    if not dp[y][x]:
        dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
        dp[y][x] = 1
        
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx

            if in_range(ny, nx) and bamboo[ny][nx] > bamboo[y][x]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)

    return dp[y][x]

answer = 0

dp = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        answer = max(answer, dfs(y, x))

print(answer)