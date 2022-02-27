import sys; input=sys.stdin.readline
import heapq

INF = sys.maxsize
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
d = [[INF]*(n+1) for _ in range(3)]

def dijkstra(idx, start):
    hq = []
    heapq.heappush(hq, (start, 0))
    d[idx][start] = 0
    while hq:
        now, dist = heapq.heappop(hq)
        if d[idx][now] < dist:
            continue
        for next in graph[now]:
            cost = d[idx][now] + next[1]  # 출발노드->거쳤다 가는 거
            if cost < d[idx][next[0]]:    # 출발노드->next 노드 바로 가는 거
                d[idx][next[0]] = cost
                heapq.heappush(hq, (next[0], cost))

for i, start in enumerate([1, v1, v2]):
    dijkstra(i, start)

answer = min(d[0][v1]+d[1][v2]+d[2][n], d[0][v2]+d[2][v1]+d[1][n])

if answer >= INF: print(-1)
else: print(answer)