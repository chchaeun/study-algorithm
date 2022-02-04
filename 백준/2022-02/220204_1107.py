# 완전 탐색
import sys; input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
if m:
    broken = list(input().split())
else:
    broken = []

answer = abs(n-100)

for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else:
        answer = min(answer, len(str(i))+abs(n-i))
    
print(answer)