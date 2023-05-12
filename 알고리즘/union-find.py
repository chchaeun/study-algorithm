def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)