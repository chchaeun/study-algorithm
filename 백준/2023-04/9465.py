import sys
input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    if n==1:
        print(max(map(max, sticker)))
        continue

    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
    dp[0][1], dp[1][1] = sticker[1][0] + sticker[0][1], sticker[0][0] + sticker[1][1]

    for i in range(2, n):
        for j in range(2):
            temp = (j+1) % 2
            dp[j][i] = max(dp[temp][i-2],dp[temp][i-1]) + sticker[j][i]
    
    print(max(dp[0][n-1], dp[0][n-2], dp[1][n-1], dp[1][n-2]))