import sys; input=sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    nlist = [input().strip() for _ in range(n)]
    nlist.sort()
    for i in range(n-1):
        if nlist[i] == nlist[i+1][:len(nlist[i])]:
            print('NO')
            break
    else:
        print('YES')