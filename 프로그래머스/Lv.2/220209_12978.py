from collections import deque

def solution(N, road, K):
    graph = [[K+1 if i!=j else 0 for j in range(N+1)] for i in range(N+1)]
    visited = [K+1 if i!=1 else 0 for i in range(N+1)]
    for r in road:
        graph[r[0]][r[1]] = min(graph[r[0]][r[1]], r[2])
        graph[r[1]][r[0]] = min(graph[r[1]][r[0]], r[2])
            
    dq = deque([(1, 0)])
    while dq:
        town, time = dq.popleft()
        for i in range(1, N+1):
            ntime = graph[town][i]+time 
            if ntime <= K and visited[i]>ntime:
                visited[i] = ntime
                dq.append((i, ntime))
    answer = 0
    for v in visited:
        if v<=K: answer+=1
    return answer

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))