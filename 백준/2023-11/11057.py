N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]
dp[0][0] = 1

for i in range(1, N):
    for j in range(10):
        dp[i][j] += sum(dp[i-1][:j+1])

print(sum([dp[N-1][i] * (10-i) for i in range(10)]) % 10007)