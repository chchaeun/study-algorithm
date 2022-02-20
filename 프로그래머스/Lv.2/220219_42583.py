from collections import deque
def solution(length, weight, trucks):
    answer = 0
    dq = deque([])
    # 공기가 있다고 생각
    for _ in range(length):
        dq.append(0)
    i=0
    _sum=0
    while i<len(trucks):
        _sum-=dq.popleft()
        answer+=1
        if _sum+trucks[i]<=weight:
            dq.append(trucks[i])
            _sum+=trucks[i]
            i+=1
        else:
            dq.append(0)
    answer+=len(dq)
    return answer

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))