import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

result = 0
a.sort()
for i in range(n):
    result += a[i]*(n-i)
    
print(result)