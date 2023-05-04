n = int(input())
numbers = [0]+list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    _max = 0
    for j in range(i):
        if numbers[j] < numbers[i] and dp[j] > _max:
            _max = dp[j]
    dp[i] = _max + 1
    
print(max(dp))