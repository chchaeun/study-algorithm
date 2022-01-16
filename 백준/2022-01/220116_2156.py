import sys
input = sys.stdin.readline

n = int(input().strip())
w = [0]+[int(input().strip()) for _ in range(n)]
d = [0 for _ in range(n+1)]
for i in range(1, n+1):
    # 선택 안하는 경우 vs 전전 거 빼고 선택하는 경우 vs 전전 거 넣고 선택하는 경우
    d[i] = max(d[i-1], d[i-3]+w[i-1]+w[i], d[i-2]+w[i])
    
print(d[n])