import sys; input=sys.stdin.readline
import heapq

INF = 1000*1000
n, e = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [INF for _ in range(n)]
print(graph)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = distance[now] + next[1]  # 출발노드->거쳤다 가는 거
            if cost < distance[next[0]]:    # 출발노드->next 노드 바로 가는 거
                distance[next[0]] = cost
                heapq.heappush(hq, (cost, next[0]))
                
dijkstra(0)

for i in range(len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])