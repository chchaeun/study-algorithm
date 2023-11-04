dp = [1] * 1001
dp[2] = 2
for i in range(3, 1001):
    dp[i] += dp[i-1]
    dp[i] += dp[i-2] - 1

N = int(input())

print(dp[N] % 10007)