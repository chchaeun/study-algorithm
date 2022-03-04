import sys; input=sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

def cycle(root, prev, next):
    visited[root] = 1
    for i in graph[next]:
        if prev!=i and i==root:
            return True
        if not visited[i]:
            visited[i] = 1
            if cycle(root, next, i):
                return True
            visited[i] = 0
    return False

answer = 0
for count in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    visited = [0 for _ in range(n)]
    if cycle(a, a, a):
        answer = count
        break
print(answer)
    
'''
그래프 문제 아님
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n)]
endgame = 0

def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y

def union(x, y, indx):
    global endgame
    x = find(x)
    y = find(y)
    if x != y:
        parents[max(x,y)] = min(x,y)
    elif endgame == 0:
        endgame = indx

for i in range(m):
    a, b = map(int, input().split())
    union(a, b, i + 1)

print(endgame)

'''