import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

dp = [[1 if i == j else 0 for j in range(N)] for i in range(N)]


for i in range(1, N):
    y, x = 0, i
    while True:
        if arr[y] == arr[x] and (x - y == 1 or dp[y + 1][x - 1] == 1):
            dp[y][x] = 1

        ny, nx = y + 1, x + 1

        if 0 <= ny < N and 0 <= nx < N:
            y, x = ny, nx
        else:
            break

for _ in range(M):
    S, E = map(int, input().split())

    print(dp[S-1][E-1])