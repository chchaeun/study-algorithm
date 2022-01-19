import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
d = [[0 for _ in range(21)] for _ in range(n)]

d[0][arr[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if d[i-1][j]:
            if 0<=j-arr[i]<=20:
                d[i][j-arr[i]] += d[i-1][j]
            if 0<=j+arr[i]<=20:
                d[i][j+arr[i]] += d[i-1][j]
                
print(d[n-2][arr[-1]])


# 더해서 만드는 문제
# 더하거나 빼서 최종값을 만드려고 하지말고
# 1, 2, 3, 4, 5, ... , n 순차적으로 만드는 방법을 찾자.