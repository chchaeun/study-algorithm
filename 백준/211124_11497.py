import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    result = -1
    for i in range(0, n-2):
        result = max(result, l[i+2]-l[i])
    print(result)