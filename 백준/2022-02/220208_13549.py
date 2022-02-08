import sys; input = sys.stdin.readline

n, k = map(int, input().split())
dp = [abs(i-n) for i in range(k*2+1)]

def around(start):
    if start+1 >= k*2 or start-1<0:
        return
    dp[start-1] = min(dp[start-1], dp[start]+1)
    dp[start+1] = min(dp[start+1], dp[start]+1)
    if dp[start-1]>dp[start]+1:
        dp[start-1] = dp[start]+1
        around(start-1, 1+1)
    else: return
    if dp[start+1]>dp[start]+1:
        dp[start-1] = dp[start]+1
    else: return
    
for i in range(0, k*2):
    temp = i
    if temp==0:
        around(temp)
    else:
        while temp < k:
            dp[temp*2] = min(dp[temp*2], dp[temp])
            around(temp*2)
            temp*=2
        
print(dp[k])
    
    
# 반례 찾는 연습하자!!