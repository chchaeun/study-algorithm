import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n)]
cycle = False
for i in range(m):
    a, b = map(int, input().split())
    if find(parent, a) == find(parent, b):
        cycle = True
        print(i+1)
        break
    else: 
        union(parent, a, b)

if not cycle:
    print(0)     
