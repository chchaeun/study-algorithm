INF = int(1e9)
N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]

answer = INF

for fix in range(3):
    dp = [c[:] for c in cost]
    for i in range(1, N):
        for j in range(3):
            if i in [1, N-1] and j == fix:
                dp[i][j] = INF
            elif i == 1:
                dp[i][j] = dp[0][fix] + dp[i][j]
            else:
                dp[i][j] = min(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3]) + dp[i][j]
    
    answer = min(min(dp[N-1]), answer)

print(answer)