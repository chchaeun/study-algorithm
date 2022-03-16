# DP
# 1) dp[i]=i 처음 한 개 있을 때 복사하고 그 뒤로 쭉 붙여넣기만 실행 
# 2) dp[i]=dp[i+1]+1 하나를 삭제한 경우 
# 3) dp[i*j]=dp[i]+j 화면에 있는 거 복사 1초 + i*j까지 붙여넣기 i-1초
'''
n = int(input())
dp = [i for i in range(1003)]
dp[1] = 0

for i in range(2, n+1):
    j = 2
    while i*j<1003:
        dp[i*j] = min(dp[i*j], dp[i]+j)
        dp[i*j-1] = min(dp[i*j]+1, dp[i*j-1])
        j+=1
print(dp[n])
'''

from collections import deque, defaultdict
n=int(input())
q = deque([(1, 0)])
visited = defaultdict(lambda: -1)
visited[(1, 0)] = 0
while q:
    s, c = q.popleft()
    # 복사
    # visited에서 s==c인 경우 필터링
    if visited[(s, s)]==-1:
        q.append((s, s))
        visited[(s, s)] = visited[(s, c)]+1
    # 붙여넣기
    # visited에서 c!=0인 경우 필터링
    if s+c<n+1 and visited[(s+c, c)]==-1:
        q.append((s+c, c))
        visited[(s+c, c)] = visited[(s, c)]+1
    # 삭제
    if 0<=s-1 and visited[(s-1, c)]==-1:
        q.append((s-1, c))
        visited[(s-1, c)] = visited[(s, c)]+1
answer = 10000        
for i in range(1, n+1):
    answer = min(answer, visited[(n, i)])
print(answer)