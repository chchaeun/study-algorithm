import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        _min = heapq.heappop(scoville)
        if _min < K:
            if not scoville:
                return -1
            sec = heapq.heappop(scoville)
            if K and not sec:
                return -1
            heapq.heappush(scoville, _min + (2 * sec))
            answer+=1
        else:
            return answer
    
print(solution([1, 2], 7))