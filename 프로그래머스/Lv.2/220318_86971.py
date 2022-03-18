from collections import defaultdict, deque
def solution(n, wires):
    answer = 1000
    wlist = [[] for _ in range(n+1)]
    for w in wires:
        wlist[w[0]].append(w[1])
        wlist[w[1]].append(w[0])
    for w in wires:
        start = min(w[0], w[1])
        answer = min(answer, abs(n-2*bfs(start, wlist, w)))
    return answer

def bfs(start, wlist, cut):
    dq = deque([start])
    visited = defaultdict(lambda: False)
    visited[(cut[0], cut[1])] = visited[(cut[1], cut[0])] = True
    count = 0
    while dq:
        cur = dq.popleft()
        count+=1
        for next in wlist[cur]:
            if not visited[(cur, next)] and not visited[(next, cur)]:
                dq.append(next)
                visited[(cur, next)] = visited[(next, cur)] = True
    return count
    
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))