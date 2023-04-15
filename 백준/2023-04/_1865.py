INF = int(1e9)
tc = int(input())

def bf(n):
    dist = [INF] * (n+1)
    dist[1] = 0
    for i in range(n):
        for edge in edges:
            cur, next, cost = edge
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n-1:
                    return True
    return False

for _ in range(tc):
    n, m, w = map(int, input().split())

    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    if bf(n):
        print('YES')
    else:
        print('NO')