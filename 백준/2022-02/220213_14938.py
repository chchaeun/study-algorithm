from collections import deque
import sys; input = sys.stdin.readline

n, m, r = map(int, input().split())
item = [0]+list(map(int, input().split()))
graph = [[m+1 if i==j else 0 for j in range(n+1)] for i in range(n+1)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = graph[b][a] = l
    
def getItems(town, n):
    dq = deque([(town, 0)])
    answer = [town]
    _sum=0
    while dq:
        ptown, pleng = dq.popleft()
        for i in range(1, n+1):
            nleng = pleng+graph[ptown][i]
            if i not in answer and nleng<=m:
                dq.append((i, nleng))
                answer.append(i)
    print(answer)
    for a in answer:
        _sum+=item[a]
    return _sum

result = 0
for i in range(1, n+1):
    result = max(result, getItems(i, n))
print(result)