from collections import deque
def solution(priorities, location):
    dq = deque(priorities)
    answer = 0
    while dq:
        if max(dq)==dq[0]:
            dq.popleft()
            answer += 1
            if location==0: break
            else: location -= 1
        else:
            dq.append(dq.popleft())
            location = len(dq)-1 if location==0 else location-1
    return answer
    
solution([2, 1, 3, 2], 2)