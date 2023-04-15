import sys; input=sys.stdin.readline
import heapq

v, e = map(int, input().split())
k = int(input())

INF = int(1e9)

graph = [[] for _ in range(v+1)] # 노드 정보
distance = [INF for _ in range(v+1)] # 최단 거리

for _ in range(e):
    u, v, w = map(int, input().split()) # 출발, 도착, 가중치
    graph[u].append((v, w))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)

        if distance[now] < dist:
            continue
        
        for next in graph[now]:
            cost = dist + next[1]  # 출발노드->거쳤다 가는 거
            
            if cost < distance[next[0]]:    # 출발노드->next 노드 바로 가는 거
                distance[next[0]] = cost
                heapq.heappush(hq, (cost, next[0])) 

dijkstra(k)

for d in distance[1:]:
    if d == INF:
        print('INF')
        continue
    print(d)