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

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n+1)]

    edges = [(c[2], c[0], c[1]) for c in costs]
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost

    return answer

print(solution(7, [[2,3,7],[3,6,13],[3,5,23],[5,6,25],[0,1,29],[1,5,34],[1,2,35],[4,5,53],[0,4,75]]))
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] ))