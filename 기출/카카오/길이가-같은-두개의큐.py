from collections import defaultdict, deque

def solution(queue1, queue2):    
    head, tail = 0, len(queue1)-1
    queue = queue1 + queue2
    _sum = sum(queue)
    if _sum%2!=0: return -1
    goal = _sum//2

    n = len(queue)    
    current = sum(queue1)
    
    dq = deque([(head, tail, current, 0)])
    dx, dy = [1, 0], [0, 1]
    visited = defaultdict(int)
    while dq:
        chead, ctail, current, count = dq.popleft()
        for i in range(2):
            nhead, ntail = (chead+dx[i])%n, (ctail+dy[i])%n
            if i==0:
                ncurrent = current - queue[chead]
            else:
                ncurrent = current + queue[ntail]
            if ncurrent==goal:
                return count + 1
            if not visited[(nhead, ntail)]:
                dq.append((nhead, ntail, ncurrent, count+1))
                visited[(nhead, ntail)] = 1
    return -1
                
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
