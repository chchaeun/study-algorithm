def solution(triangle):
    h = len(triangle)
    
    dp = [[0 for _ in range(h + 1)] for _ in range(h+1)]

    for i in range(h):
        for j in range(h):
            if len(triangle[i]) <= j:
                continue
            dp[i+1][j+1] = triangle[i][j] + max(dp[i][j], dp[i][j+1])
    
    return max(dp[h])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))