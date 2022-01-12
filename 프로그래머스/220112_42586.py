import math

def solution(progresses, speeds):
    n = len(progresses)
    _max = math.ceil((100-progresses[0])/speeds[0])
    count = 1
    answer = []
    for i in range(1, n):
        cur = math.ceil((100-progresses[i])/speeds[i])
        if cur > _max:
            answer.append(count)
            count = 1
            _max = cur
        else:
            count += 1
    answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([99, 99, 99, 99, 99, 99], [1, 1, 1, 1, 1, 1]))
            
    