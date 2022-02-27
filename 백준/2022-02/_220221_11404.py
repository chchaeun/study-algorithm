# 플로이드-와샬 알고리즘
# https://blog.naver.com/ndb796/221234427842
import sys; input=sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
INF = 100001*100
cost = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)
    
for k in range(1, n+1):
    for i in range(1, n+1):
        if i==k: continue
        for j in range(1, n+1):
            if i==j or j==k: continue
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
for i in cost[1:]:
    for j in i[1:]:
        if j==INF:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()