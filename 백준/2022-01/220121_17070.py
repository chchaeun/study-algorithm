import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(2, n):
    if board[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]
        
# (0, 1) 칸에서 출발하기 때문에 (1, 2)부터 반복
for i in range(1, n):
    for j in range(2, n):
        if board[i][j] == 0:
            # 대각선 파이프는 (i, j), (i-1, j), (i, j-1) 총 세 칸을 차지한다.
            # 모두 비어있어야 진행 가능
            if board[i-1][j] == 0 and board[i][j-1] == 0:
                dp[i][j][2] = sum(dp[i-1][j-1])
                
            # 가로 파이프는 (i, j-1)에서 온다.
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            
            # 세로 파이프는 (i-1, j)에서 온다.
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            
print(sum(dp[n-1][n-1]))