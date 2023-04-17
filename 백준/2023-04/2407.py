n, m = map(int, input().split())
if n-m < m:
    m = n-m

answer = 1
for i in range(m):
    answer *= n-i
    answer //= i+1

print(answer)