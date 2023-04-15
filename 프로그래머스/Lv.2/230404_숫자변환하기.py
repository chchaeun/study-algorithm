def solution(x, y, n):
    if x == y:
        return 0 

    dp = [0 for _ in range(y + 1)]

    for i in range(x+1, y+1):
        if i-n >= x:
            dp[i] = dp[i-n] + 1
        
        if i%3 == 0 and i//3 >= x:
            dp[i] = min(dp[i//3] + 1, dp[i])

        if i%2 == 0 and i//2 >= x:
            dp[i] = min(dp[i//2] + 1, dp[i])
        
    if dp[y] == 0:
        return -1

    return dp[y]

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))
print(solution(10, 10, 5))
print(solution(1, 1000000, 999999))