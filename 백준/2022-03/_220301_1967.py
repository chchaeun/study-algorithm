# 트리의 지름 증명
# https://koosaga.com/14
from collections import deque
import sys; input=sys.stdin.readline

n = int(input().strip())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
    
    
def bfs(start, mode):
    dist = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    visited[start]=1
    dq = deque([(start, 0)])
    while dq:
        cnode, cdist= dq.popleft()
        for next in tree[cnode]:
            nnode, ndist = next[0], next[1]
            if visited[nnode]==0:
                dist[nnode] = cdist+ndist
                dq.append((nnode, dist[nnode]))
                visited[nnode]=1
    if mode: return dist.index(max(dist))
    else: return max(dist)
print(bfs(bfs(1, 1),0))

    

# def dijkstra(start, mode):
#     hq = []
#     visited = [0 for _ in range(n+1)]
#     dist = [0 for _ in range(n+1)]
#     heapq.heappush(hq, (0, start))
#     while hq:
#         now_dist, now_node = heapq.heappop(hq)
#         for next in tree[now_node]:
#             next_node, next_dist = next[0], next[1]
#             cost = -now_dist+next_dist
#             if visited[next_node]==0 and cost > dist[next_node]:
#                 dist[next_node] = cost
#                 heapq.heappush(hq, (-cost, next_node))
#                 visited[next_node] = 1
#     if mode: return dist.index(max(dist))
#     else: return max(dist)

# print(dijkstra(dijkstra(1, 1), 0))
    

