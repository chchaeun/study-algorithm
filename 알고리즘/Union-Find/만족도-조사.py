n, m, k = map(int, input().split())
satis = [0 for _ in range(n+1)]
for _ in range(m):
    i, s = map(int, input().split())
    satis[i] = s
relation = [list(map(int, input().split())) for _ in range(k)]

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(u, v):
    u, v = find(u), find(v)
    if u<v: parent[v] = u
    else: parent[u] = v
    
for u, v in relation:
    union(u, v)

def avg(x):
    p = parent[x]
    _sum, count = 0, 0
    for i in range(1, n+1):
        if i!=x and parent[i] == p:
            _sum += satis[i]
            count += 1
    satis[x] = _sum//count if count!=0 else 0

_sum, count = 0, 0
for i in range(1, n+1):
    if satis[i]==0: avg(i)
    if satis[i]!=0:
        _sum += satis[i]
        count += 1
print(_sum, count)
print(round(_sum/count, 2))