from collections import defaultdict

def solution(k, tangerine):
    size = defaultdict(int)

    for t in tangerine:
        size[t] += 1

    hq = list(size.values())
    hq.sort(reverse=True)
    
    sum = 0
    answer = 0
    for h in hq:
        sum += h
        answer += 1
        if sum >= k:
            return answer


print(solution(6, [1,3,2,5,4,5,2,3]))
print(solution(4, [1,3,2,5,4,5,2,3]))
print(solution(2, [1,1,1,1,2,2,2,3]))