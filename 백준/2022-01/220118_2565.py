import sys
input = sys.stdin.readline

n = int(input().strip())
line = [list(map(int, input().split())) for _ in range(n)]
line.sort(key=lambda x: x[0])
LIS = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            LIS[i] = max(LIS[i], LIS[j]+1)
            
print(n-max(LIS))