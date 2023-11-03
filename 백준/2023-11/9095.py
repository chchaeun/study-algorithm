dp = [0] * 12
dp[0] = 1

for i in range(1, 12):
    if i - 3 >= 0:
        dp[i] += dp[i-3]
    if i - 2 >= 0:
        dp[i] += dp[i-2]
    
    dp[i] += dp[i-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])