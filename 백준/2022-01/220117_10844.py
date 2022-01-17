n = int(input())
d = [[0 for _ in range(11)] for _ in range(n)]

for i in range(0, 10):
    d[0][i] = 1
    
for i in range(1, n):
    for j in range(0, 10):
        d[i][j] = d[i-1][j-1]+ d[i-1][j+1]

print((sum(d[n-1])-d[n-1][0])%1000000000)

# 1의 자리 수에서 1~9까지 몇 번 나오는지 체크

for i in d:
    print(*i)