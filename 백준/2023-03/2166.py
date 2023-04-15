import sys
input = sys.stdin.readline
n = int(input().rstrip())
point = [list(map(int, input().split())) for _ in range(n)]
point = point + [point[0]]

sum = 0
for i in range(n):
    sum += point[i][0] * point[i+1][1] - point[i][1] * point[i+1][0]

print(round(abs(sum)/2, 2))