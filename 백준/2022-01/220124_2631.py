import sys
input = sys.stdin.readline

# 일렬로 서있는 아이들 중에 줄에 맞지 않게 서있는 아이들 이동
# 줄에 맞게 서있는 애들 -> 최대한 많아야 함
# 최장증가 부분수열

n = int(input().strip())
line = [int(input().strip()) for _ in range(n)]
LIS = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if line[j]<line[i]:
            LIS[i] = max(LIS[j]+1, LIS[i])

print(n-max(LIS))
