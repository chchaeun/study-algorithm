global answer, far
answer = 0
far = 0

V = int(input())
edges = [[] for _ in range(V+1)]

for _ in range(V):
    temp = list(map(int, input().split()))
    num = temp[0]
    for i in range(1, len(temp)-1, 2):
        edges[num].append([temp[i], temp[i+1]])

def dfs(current, visited, total):
    global answer, far

    if total > answer:
        answer = total
        far = current

    for edge in edges[current]:
        next, dist = edge

        if not visited[next]:
            visited[next] = True
            dfs(next, visited, total + dist)
            visited[next] = False

visited = [False for _ in range(V+1)]
visited[i] = True

dfs(i, visited, 0)

visited = [False for _ in range(V+1)]
visited[far] = True

dfs(far, visited, 0)

print(answer)
