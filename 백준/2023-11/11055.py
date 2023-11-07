N = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j])

print(max(dp))